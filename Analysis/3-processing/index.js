const dir = './scripts/';
const fs = require('fs');
const process = require('process');
const wNumb = require('wnumb');
const sedyl = require('./sedyl');
const papa = require('papaparse');
const moment = require('moment');
const _ = require('underscore');
const Papa = require('papaparse');
const ss = require('simple-statistics');
const format = wNumb({
    decimals: 2,
});
const DEBUG = true
const DELAY_BETWEEN_LAPTOP_EVENT = 5 //minutes
const MIN_DELAY_BETWEEN_LAPTOP_EVENT = 2 //minutes
const FILENAME_FILTERED_LAPTOP = './data/laptop_filtered.csv';
const FILENAME_FILTERED_FORECAST = './data/forecast_filtered.csv';

DEBUG && console.log('Loading files...');
const laptopFile = fs.readFileSync(FILENAME_FILTERED_LAPTOP, 'utf8')
const forecastFile = fs.readFileSync(FILENAME_FILTERED_FORECAST, 'utf8')

var laptopList = papa.parse(laptopFile, {
    header: true,
    delimiter: ','
}).data
var forecastList = papa.parse(forecastFile, {
    header: true,
    delimiter: ','
}).data.filter(forecast => moment(forecast.timestamp).isValid())

DEBUG && console.log('Extracting users...');
var userSet = [...new Set(laptopList.map(laptop => laptop.username).filter(user => user != undefined))];
DEBUG && console.log('Extracting forecast days...');
var forecastDaySet = [...new Set(forecastList.map(forecast => moment(forecast.timestamp).hours(0).minutes(0).seconds(0).milliseconds(0).format()))]


DEBUG && console.log('Removing unrelevant forecast days...');
forecastDaySet = forecastDaySet.filter(forecastDay => {
    start = moment(forecastDay).hours(0).minutes(0).seconds(0)
    end = moment(forecastDay).hours(23).minutes(59).seconds(59)
    forecastDayList = forecastList.filter(forecast => moment(forecast.timestamp).isBetween(start, end))
    forecastValueList = forecastDayList.map(forecast => parseFloat(forecast.production))
    var dechargeDuration = 3
    var threshold = 0.12
    var variationIndexes = getIndexesVariations(forecastValueList)
    for (var i = 0; i < variationIndexes.length - 1; i++) {
        var variation = forecastValueList.filter((forecast, j) => (variationIndexes[i] <= j && j <= variationIndexes[i + 1]))
        var argpeakVariation = variation.indexOf(Math.max(...variation));
        var argAscendingVariation = Math.max(argpeakVariation, 0)
        var startAscendingVariation = argpeakVariation - Math.min(argAscendingVariation, dechargeDuration)
        var ascendingVariation = variation.slice(startAscendingVariation, argpeakVariation)
        if (ascendingVariation.length) {
            var ascendingScore = ss.mean(ascendingVariation)
            var maxScore = Math.max(variation)
            var score = maxScore - ascendingScore
            if (score < threshold) {} else {
                return forecastDay;
            }
        }
    }
})

laptopList = laptopList.filter(laptop => forecastDaySet.includes(moment(laptop.timestamp).hours(0).minutes(0).seconds(0).format()))
forecastList = forecastList.filter(forecast => forecastDaySet.includes(moment(forecast.timestamp).hours(0).minutes(0).seconds(0).format()))

startHourDays = laptopList.map(laptop => moment(laptop.timestamp).hours(0).minutes(0).seconds(0).milliseconds(0))
startHourDays = startHourDays.filter((v, i) => {
    return startHourDays.findIndex(candidate => v.isSame(candidate)) == i
});
endHourDays = laptopList.map(laptop => moment(laptop.timestamp).hours(23).minutes(59).seconds(59).milliseconds(0))
endHourDays = endHourDays.filter((v, i) => {
    return endHourDays.findIndex(candidate => v.isSame(candidate)) == i
});


var ans = {};
DEBUG && console.log('Removing unrelevant usages...');
_.map(_.zip(startHourDays, endHourDays), pair => {
    var startHourDay = pair[0]
    var endHourDay = pair[1]
    forecastDay = forecastList.filter(forecast => moment(forecast.timestamp).isBetween(startHourDay, endHourDay))
    inputForecastList = []
    forecastDay.map(forecast => {
        m = moment(forecast.timestamp)
        inputForecastList.push(m.format('kk:mm') + ',' + forecast.production)
    });

    if (inputForecastList.length > 0) {
        laptopDay = laptopList.filter(laptop => moment(laptop.timestamp).isBetween(startHourDay, endHourDay))
        userSet.map(user => {
            laptopDayUser = laptopDay.filter(laptop => laptop.username === user);
            for (var i = 0; i < laptopDayUser.length - 1; i++) {
                currLaptop = laptopDayUser[i];
                nextLaptop = laptopDayUser[i + 1];
                usage = {}
                usage.startMoment = moment(currLaptop.timestamp)
                usage.startStorage = Math.min(parseInt(currLaptop.storage), 100)
                diffTimestamp = MIN_DELAY_BETWEEN_LAPTOP_EVENT <= moment(nextLaptop.timestamp).diff(moment(currLaptop.timestamp), 'minutes') <= DELAY_BETWEEN_LAPTOP_EVENT;
                diffUsage = nextLaptop.usage === currLaptop.usage;
                var j = i;
                while (j + 1 < laptopDayUser.length - 1 && diffTimestamp && diffUsage) {
                    j++;
                    currLaptop = laptopDayUser[j];
                    nextLaptop = laptopDayUser[j + 1];
                    diffTimestamp = MIN_DELAY_BETWEEN_LAPTOP_EVENT <= moment(nextLaptop.timestamp).diff(moment(currLaptop.timestamp), 'minutes') <= DELAY_BETWEEN_LAPTOP_EVENT;
                    diffUsage = nextLaptop.usage === currLaptop.usage

                }
                usage.endMoment = moment(currLaptop.timestamp)
                usage.endStorage = Math.min(parseInt(currLaptop.storage), 100)
                usage.mode = currLaptop.usage
                DEBUG && process.stdout.write('[' + usage.mode + '] from [' + usage.startMoment.format('kk:mm') + ' at ' + usage.startStorage + '%] to [' + usage.endMoment.format('kk:mm') + ' at ' + usage.endStorage + '%]...')
                if (j - i < 1) {
                    DEBUG && console.log('Rejected!')
                } else {
                    DEBUG && console.log('Accepted!');
                    var ans = computeScore(usage, inputForecastList);
                    DEBUG && console.log('------ SCORE ------');
                    DEBUG && console.log(ans);
                    DEBUG && console.log('-------------------');
                }
                i = j;
            }
        });
    }
});

/**
 * Return the energy saving + shifting (Wh) of the given usage for the given energy production
 * @param {*} usage 
 * @param {*} production 
 */
function computeScore(usage, production) {
    script = {
        "input_production": "",
        "input_usage": "",
        "step": "1",
        "q_rated": "8.8",
        "v_nom": "11.1",
        "a_charge": "8.8",
        "a_discharge": "1.44",
        "soc_min": "1",
        "soc_max": "100",
        "soc": "0",
        "soc_enr": "50",
        "battery_efficiency": "90",
        "charger_efficiency": "80"
    }
    script.soc = usage.startStorage.toString();
    script.input_production = production.join('\n');
    script.input_usage = usage.startMoment.format('kk:mm') + ',' + usage.startStorage + ',' + usage.endMoment.format('kk:mm') + ',' + usage.endStorage + ',' + usage.mode;
    var {
        computationAnomList,
        batteryAnomList
    } = sedyl.adjust(script)

    if (batteryAnomList.length) script.a_charge = batteryAnomList[0].toString();
    if (computationAnomList.length) script.a_discharge = computationAnomList[0].toString();
    currentUsage = sedyl.run(script);

    script.input_usage = usage.startMoment.format('kk:mm') + ',' + usage.startStorage + ',' + usage.endMoment.format('kk:mm') + ',' + usage.endStorage + ',' + 'battery_sector';
    if (batteryAnomList.length) script.a_charge = batteryAnomList[0].toString();
    if (computationAnomList.length) script.a_discharge = computationAnomList[0].toString();
    referenceUsage = sedyl.run(script)
    //DEBUG && console.log(practice, currentPractice.diff(format, referencePractice))
    return currentUsage.diff(format, referenceUsage);
}

/**
 * Get the indexes of the variations for the given time series
 * @param {*} usages 
 */
function getIndexesVariations(usages) {
    var variations = [0];
    for (var i = 1; i < usages.length - 1; i++) {
        prev_production = usages[i - 1]
        curr_production = usages[i]
        next_production = usages[i + 1]
        if (prev_production > curr_production && next_production > curr_production) {
            variations.push(i)
        } else if (prev_production > curr_production && next_production == curr_production) {
            var j = i + 1;
            while (j < usages.length - 1 && next_production == curr_production) {
                curr_production = usages[j]
                next_production = usages[j + 1]
                j += 1;
            }
            if (j < usages.length - 1 && next_production > curr_production) {
                variations.push(i);
            }
        }
    }
    variations.push(usages.length - 1);
    return variations;
}