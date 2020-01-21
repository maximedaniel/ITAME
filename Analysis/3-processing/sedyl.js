const RESOLUTION = 0.001;
const fs = require('fs')
const wNumb = require('wnumb')
const moment = require('moment')
const twix = require('twix')
const Papa = require('papaparse')
const everpolate = require('everpolate')
const ss = require('simple-statistics')
const clone = require('lodash').cloneDeep


    class Practice {
        constructor(name, parameters, production, usages, battery, computation, sector) {
            compute(usages.list[0], computation, battery, sector);
            this.name = name
            this.usages = parameters.input_usage.split('\n');
            this.enr = ss.sum(sector.consumption_enr) || 0
            this.total = ss.sum(sector.consumption_total) || 0
            this.nenr = this.total - this.enr
            this.mean_enr = (this.enr / this.total) * 100 || 0
            this.mean_nenr = (this.nenr / this.total) * 100 || 0

            this.time = [];
            this.production_enr = [];
            this.production_total = [];
            this.battery_storage_enr = [];
            this.battery_storage_total = [];
            this.battery_consumption_enr = [];
            this.battery_consumption_total = [];
            this.computation_consumption_enr = [];
            this.computation_consumption_total = [];
            this.sector_consumption_enr = [];
            this.sector_consumption_total = [];

            var now = moment()
            Papa.parse(parameters.input_production).data.forEach((e) => {
                var time = moment(now.format('YYYY-MM-DD ') + e[0].trim());
                this.time.push(time);
                var indexTime = -1;

                if(production.time.length) indexTime = production.time.findIndex(moment => moment.isSame(time));
                if(indexTime) {
                    this.production_enr.push(production.enr[indexTime]);
                    this.production_total.push(production.total[indexTime]);
                }
                
                if(battery.time.length) {
                    //console.log(time, battery.time)
                    indexTime = battery.time.findIndex(moment => moment.isSame(time));
                }
                if(indexTime) {
                    this.battery_storage_enr.push(ss.sum(battery.storage_enr.slice(0, indexTime)));
                    this.battery_storage_total.push(ss.sum(battery.storage_total.slice(0, indexTime)));
                    this.battery_consumption_enr.push(ss.sum(battery.consumption_enr.slice(0, indexTime)));
                    this.battery_consumption_total.push(ss.sum(battery.consumption_total.slice(0, indexTime)));
                }

                if(computation.time.length) indexTime = computation.time.findIndex(moment => moment.isSame(time));
                if(indexTime) {
                    this.computation_consumption_enr.push(ss.sum(computation.consumption_enr.slice(0, indexTime)));
                    this.computation_consumption_total.push(ss.sum(computation.consumption_total.slice(0, indexTime)));
                }

                if(sector.time.length) indexTime = sector.time.findIndex(moment => moment.isSame(time));
                if(indexTime) {
                    this.sector_consumption_enr.push(ss.sum(sector.consumption_enr.slice(0, indexTime)));
                    this.sector_consumption_total.push(ss.sum(sector.consumption_total.slice(0, indexTime)));
                }
            });
        }

        print(format) {
            console.log('total : ', format.to(this.total) + 'Wh')
            console.log('total_enr : ', format.to(this.enr) + 'Wh (' + format.to(this.mean_enr) + '%)')
            console.log('total_nenr : ', format.to(this.nenr) + 'Wh (' + format.to(this.mean_nenr) + '%)')
        }

        diff(format, practice) {
            var total_diff = this.total - practice.total
            var mean_total_diff = (total_diff / this.total) * 100
            if (!isFinite(mean_total_diff)) mean_total_diff = 0
            var mean_enr_diff = this.mean_enr - practice.mean_enr
            var mean_nenr_diff = this.mean_nenr - practice.mean_nenr
            var enr_diff = this.total * mean_enr_diff / 100
            var nenr_diff = this.total * mean_nenr_diff / 100
            var score_saving = practice.total - this.total
            var score_shifting = practice.nenr - this.nenr
            var percentage_shifting = (score_shifting / practice.nenr) * 100
            var score_total = score_shifting + score_saving
            return {
                'total_curr': this.total,
                'total_ref': practice.total,
                'nenr_curr': this.nenr, 
                'nenr_ref': practice.nenr, 
                'total_diff': total_diff,
                'enr_diff': enr_diff,
                'nenr_diff': nenr_diff,
                'score_saving': score_saving,
                'score_shifting': score_shifting,
                'percentage_shifting': percentage_shifting,
                'score_total': score_total
            }
        }
    }

    class Parameters {
        constructor(json) {
            for (var prop in json) this[prop] = json[prop]
        }
    }

    class Production {
        constructor(parameters) {
            var time = []
            var value = []
            var now = moment()
            Papa.parse(parameters.input_production).data.forEach(function (e) {
                time.push(moment(now.format('YYYY-MM-DD ') + e[0].trim()))
                value.push(parseFloat(e[1]))
            });
            var step = parseInt(parameters.step)
            var time_interpolated = moment.twix(time[0], time[time.length - 1]).toArray(step, 'minutes')
            var step_interpolation = everpolate.step
            var value_interpolated = step_interpolation(time_interpolated, time, value)
            var time = []
            var enr = []
            var total = []
            time_interpolated.forEach(function (e) {
                time.push(e)
            });
            value_interpolated.forEach(function (e) {
                enr.push(e)
            });
            value_interpolated.forEach(function (e) {
                total.push(1.)
            });
            this.time = time
            this.enr = enr
            this.total = total
        }
        print(format) {
            console.log(format.to(this.total) + 'Wh')
            console.log(format.to(this.enr) + 'Wh (' + format.to(this.mean_enr) + '%)')
            console.log(format.to(this.nenr) + 'Wh (' + format.to(this.mean_nenr) + '%)')
        }
        statistics() {
            console.log("production_mean : ", (ss.mean(this.enr) * 100).toFixed(1) + ' %')
            console.log("production_mean : ", (ss.standardDeviation(this.enr) * 100).toFixed(1) + ' %')
        }
    }

    class Usage {
        constructor(mode, time, enr, total, start_soc, end_soc) {
            this.mode = mode;
            this.time = time;
            this.enr = enr;
            this.total = total;
            this.start_soc = start_soc;
            this.end_soc = end_soc;
        }
        toString(){
            return [...this.time.map(String)];
        }
    }

    class Usages {
        constructor(parameters, production) {
            this.time = [];
            this.list = [];
            var time_g = this.time;
            production.time.forEach(function (e) {
                time_g.push(e)
            });
            var now = moment();
            Papa.parse(parameters.input_usage).data.forEach((e) => {
                var time_start = moment(now.format('YYYY-MM-DD ') + e[0].trim());
                var start_soc = parseInt(e[1].trim())/100.;
                var time_end = moment(now.format('YYYY-MM-DD ') + e[2].trim());
                var end_soc = parseInt(e[3].trim())/100.;
                var mode = e[4].trim();
                var step_interpolation = everpolate.step;
                var time = production.time.filter(function (t) {
                    return (t >= time_start && t <= time_end);
                });
                var enr = step_interpolation(time, production.time, production.enr);
                var total = step_interpolation(time, production.time, production.total);

                /* identifiy Q */
                var usage = new Usage(mode, time, enr, total, start_soc, end_soc);
                this.list.push(usage);
            });
            //console.log(this.list.map(usage => usage.toString()));
        }
    }

    class Battery {
        constructor(parameters) {
            this.q_rated = parseFloat(parameters.q_rated);
            this.q_exp = parseFloat(parameters.q_rated) * 0.2;
            this.v_nom = parseFloat(parameters.v_nom);
            this.v_max = parseFloat(parameters.v_nom) * 1.2;
            this.v_min = parseFloat(parameters.v_nom) * 0.2;
            this.a_nom = parseFloat(parameters.a_charge);
            this.soc_max = parseFloat(parameters.soc_max) / 100;
            this.soc_min = parseFloat(parameters.soc_min) / 100;
            this.soc = parseFloat(parameters.soc) / 100;
            this.soc_enr = parseFloat(parameters.soc_enr) / 100;
            this.battery_efficiency = parseFloat(parameters.battery_efficiency) / 100;
            this.r_enr = this.soc_enr / this.soc; // Ah
            this.time = [];
            this.consumption_enr = [];
            this.consumption_total = [];
            this.storage_enr = [];
            this.storage_total = [];
            this.socs_enr = [];
            this.socs_total = [];
        }
        init(time) {
            this.time.push(time);
            this.consumption_enr.push(0);
            this.consumption_total.push(0);
            this.storage_enr.push(this.getChargeVoltageAt(this.soc) * this.soc_enr * this.q_rated);
            this.storage_total.push(this.getChargeVoltageAt(this.soc) * this.soc * this.q_rated);
            this.socs_enr.push(this.soc_enr);
            this.socs_total.push(this.soc);
        }


        push(time, consumption_enr, consumption_total, storage_enr, storage_total, soc_enr, soc) {
            this.time.push(time);
            this.consumption_enr.push(consumption_enr);
            this.consumption_total.push(consumption_total);
            this.storage_enr.push(storage_enr);
            this.storage_total.push(storage_total);
            this.socs_enr.push(soc_enr);
            this.socs_total.push(soc);
        }

        getChargeVoltage() {
            var E = this.v_nom;
            var Q = this.q_rated;
            var R = 0.01;
            var K = 0.0076;
            var it = Q * (1 - this.soc);
            var A = this.q_exp;
            var B = 3 / this.q_exp;
            var i = this.a_nom;
            var i_filtered = 0;
            var ans = E - R * i - K * (Q / (it - 0.1 * Q)) * i_filtered - K * (Q / (Q - it)) * it + A * Math.exp(-B * it);
            return ans;
        }
        getChargeVoltageAt(soc) {
            var E = this.v_nom;
            var Q = this.q_rated;
            var R = 0.01;
            var K = 0.0076;
            var it = Q * (1 - soc);
            var A = this.q_exp;
            var B = 3 / this.q_exp;
            var i = this.a_nom;
            var i_filtered = 0;
            var ans = E - R * i - K * (Q / (it - 0.1 * Q)) * i_filtered - K * (Q / (Q - it)) * it + A * Math.exp(-B * it);
            return ans;
        }
        canDischarge(computation) {
            return (this.soc > this.soc_min);
        }

        getDischargeVoltage() {
            var E = this.v_nom;
            var Q = this.q_rated;
            var R = 0.01;
            var K = 0.0076;
            var it = Q * (1 - this.soc);
            var A = this.q_exp;
            var B = 3 / this.q_exp;
            var i = this.a_nom;
            var i_filtered = 0;
            var ans = E - (R * i) - K * (Q / (Q - it)) * (it + i_filtered) + A * Math.exp(-B * it);
            return ans;
        }
        getDischargeVoltageAt(soc) {
            var E = this.v_nom;
            var Q = this.q_rated;
            var R = 0.01;
            var K = 0.0076;
            var it = Q * (1 - soc);
            var A = this.q_exp;
            var B = 3 / this.q_exp;
            var i = this.a_nom;
            var i_filtered = 0;
            var ans = E - (R * i) - K * (Q / (Q - it)) * (it + i_filtered) + A * Math.exp(-B * it);
            return ans;
        }
    }
    class Sector {
        constructor(parameters) {
            this.time = [];
            this.consumption_enr = [];
            this.consumption_total = [];
            this.charger_efficiency = parseFloat(parameters.charger_efficiency) / 100;
        }
        init(time) {
            this.time.push(time);
            this.consumption_enr.push(0);
            this.consumption_total.push(0);
        }
        push(time, enr, total) {
            this.time.push(time);
            this.consumption_enr.push(enr / this.charger_efficiency);
            this.consumption_total.push(total / this.charger_efficiency);
        }
    }

    class Computation {
        constructor(parameters) {
            this.v_nom = parseFloat(parameters.v_nom);
            this.a_nom = parseFloat(parameters.a_discharge);
            this.p = this.v_nom * this.a_nom;
            this.time = [];
            this.consumption_enr = [];
            this.consumption_total = [];
        }
        init(time) {
            this.time.push(time);
            this.consumption_enr.push(0);
            this.consumption_total.push(0);
        }
        push(time, enr, total) {
            this.time.push(time);
            this.consumption_enr.push(enr);
            this.consumption_total.push(total);
        }
    }

    function getTimeForFullCharge(parameters, batteryAnom, currSoc){
                var battery = new Battery(parameters);
                battery.soc = currSoc;
                battery.a_nom = batteryAnom;

                var step = 60;
                var startTimeForFullCharge = moment();
                var startBatteryLevel = battery.soc;
                var endTimeForFullCharge = moment(startTimeForFullCharge);
                var endBatteryLevel = battery.soc;
                var v_max = battery.getChargeVoltageAt(battery.soc_max);
                var v_current = battery.getChargeVoltage();
                var q_current = battery.soc * battery.q_rated;
                var a_current = battery.a_nom;
                //console.log('battery.a_current:', a_current)

                while(v_current < v_max){
                    endTimeForFullCharge.add(step, 'seconds');
                    v_current = battery.getChargeVoltage();
                    q_current = battery.soc * battery.q_rated;
                    a_current = battery.a_nom;
                    if (v_current > battery.v_nom) {
                        var factor = (v_max - v_current) / (v_max - battery.v_nom);
                        var soc_factor = Math.min(Math.max(0.0, 1 - ((1 - battery.soc) / 0.25)), battery.soc_max);
                        var a_factor = a_current - (0.03 * battery.q_rated);
                        a_current = battery.a_nom - soc_factor * a_factor;
                    }
                    var e_current = v_current * q_current;
                    var q_step = a_current * (step / 3600);
                    var e_step_total = v_current * a_current * (step / 3600);

                    var q_step = q_step * battery.battery_efficiency;
                    var e_step_total = e_step_total * battery.battery_efficiency;

                    var q_next = q_current + q_step;
                    var soc_next = q_next / battery.q_rated;
                    battery.soc = soc_next;
                    endBatteryLevel = battery.soc; 
                }
                return moment.duration(endTimeForFullCharge.diff(startTimeForFullCharge)).asMinutes();
                //console.log('Charge -> ', startTimeForFullCharge, startBatteryLevel, endTimeForFullCharge, endBatteryLevel);
                //console.log('Duration for full charge :', endTimeForFullCharge.diff(startTimeForFullCharge));
    }
    function getSocAfterChargeDuration(parameters, currSoc, batteryAnom, duration){
        var battery = new Battery(parameters);
        battery.soc = currSoc;
        battery.a_nom = batteryAnom;
        var step = 60;
        var startTimeForFullCharge = moment();
        var endTimeForFullCharge = moment(startTimeForFullCharge).add(duration, 'minutes');
        //console.log('getSocAfterChargeDuration() -> batteryAnom ->', batteryAnom);
        //console.log('getSocAfterChargeDuration -> duration ->', moment.duration(endTimeForFullCharge.diff(startTimeForFullCharge)).asMinutes());
        var v_max = battery.getChargeVoltageAt(battery.soc_max);
        var v_current = battery.getChargeVoltage();
        var q_current = battery.soc * battery.q_rated;
        var a_current = battery.a_nom;
        //console.log('battery.a_current:', a_current)
        var it = 0;
        while(endTimeForFullCharge.diff(startTimeForFullCharge, 'seconds') > 0){
            startTimeForFullCharge.add(step, 'seconds');
            v_current = battery.getChargeVoltage();
            q_current = battery.soc * battery.q_rated;
            a_current = battery.a_nom;
            if (v_current > battery.v_nom) {
                var factor = (v_max - v_current) / (v_max - battery.v_nom);
                var soc_factor = Math.min(Math.max(0.0, 1 - ((1 - battery.soc) / 0.25)), battery.soc_max);
                var a_factor = a_current - (0.03 * battery.q_rated);
                a_current = battery.a_nom - soc_factor * a_factor;
            }
            var e_current = v_current * q_current;
            var q_step = a_current * (step / 3600);
            var e_step_total = v_current * a_current * (step / 3600);

            var q_step = q_step * battery.battery_efficiency;
            var e_step_total = e_step_total * battery.battery_efficiency;

            var q_next = q_current + q_step;
            var soc_next = q_next / battery.q_rated;
            var soc_next = Math.min(soc_next, battery.soc_max);
            battery.soc = soc_next; 
            //console.log('getSocAfterChargeDuration() -> ', battery.soc, '(',it,')')
            it++;
        }
        return battery.soc;
        //console.log('Charge -> ', startTimeForFullCharge, startBatteryLevel, endTimeForFullCharge, endBatteryLevel);
        //console.log('Duration for full charge :', endTimeForFullCharge.diff(startTimeForFullCharge));
}
    function getTimeForFullDischarge(parameters, computationAnom, currSoc){
        var battery = new Battery(parameters);
        battery.soc = currSoc;
        //battery.a_nom = batteryAnom;
        var computation = new Computation(parameters);
        computation.a_nom = computationAnom;

        var step = 60;
        var startTimeForFullDischarge = moment();
        var startBatteryLevel = battery.soc;
        var endTimeForFullDischarge = moment(startTimeForFullDischarge);
        var endBatteryLevel = battery.soc;
        var v_min = battery.getDischargeVoltageAt(battery.soc_min);
        var v_current = battery.getDischargeVoltage();
        var q_current = battery.soc * battery.q_rated;
        //console.log('computation.a_nom:', computation.a_nom)

        while(v_current > v_min){
            endTimeForFullDischarge.add(step, 'seconds');
            v_current = battery.getDischargeVoltage();
            q_current = battery.soc * battery.q_rated;
            e_current = battery.getDischargeVoltage() * q_current;
            var q_step = computation.a_nom * (step / 3600);
            var q_next = Math.max(q_current - q_step, battery.soc_min * battery.q_rated);
            battery.soc = Math.max(q_next / battery.q_rated, battery.soc_min);
            endBatteryLevel = battery.soc; 
        }
        return moment.duration(endTimeForFullDischarge.diff(startTimeForFullDischarge)).asMinutes();
        //console.log('Discharge -> ', startTimeForFullCharge, startBatteryLevel, endTimeForFullCharge, endBatteryLevel);
        //console.log('Duration for full discharge :', endTimeForFullCharge.diff(startTimeForFullCharge));
    }

    function getSocAfterDischargeDuration(parameters, currSoc, computationAnom, duration){
        var battery = new Battery(parameters);
        battery.soc = currSoc;
        //battery.a_nom = batteryAnom;
        var computation = new Computation(parameters);
        computation.a_nom = computationAnom;
        //console.log(' battery.soc:',  battery.soc)
        var step = 60;
        var startTimeForFullDischarge = moment();
        var startBatteryLevel = battery.soc;
        var endTimeForFullDischarge = moment(startTimeForFullDischarge).add(duration, 'minutes');
        //console.log('getSocAfterDishargeDuration() -> computationAnom ->', computationAnom);
        //console.log('getSocAfterDishargeDuration() -> duration ->', moment.duration(endTimeForFullDischarge.diff(startTimeForFullDischarge)).asMinutes());
        var endBatteryLevel = battery.soc;
        var v_min = battery.getDischargeVoltageAt(battery.soc_min);
        var v_current = battery.getDischargeVoltage();
        var q_current = battery.soc * battery.q_rated;
        var it = 0;
        while(endTimeForFullDischarge.diff(startTimeForFullDischarge, 'seconds') > 0){
            startTimeForFullDischarge.add(step, 'seconds');
            v_current = battery.getDischargeVoltage();
            q_current = battery.soc * battery.q_rated;
            e_current = battery.getDischargeVoltage() * q_current;
            var q_step = computation.a_nom * (step / 3600);
            var q_next = Math.max(q_current - q_step, battery.soc_min * battery.q_rated);
            battery.soc = Math.max(q_next / battery.q_rated, battery.soc_min);
            endBatteryLevel = battery.soc; 
            //console.log('getSocAfterDischargeDuration() -> ', battery.soc, '(',it,')')
            it++;
        }
        return battery.soc;
    }

    function compute(usage, computation, battery, sector) {

        var m_current = moment(usage.time[0]);
        var m_end = moment(usage.time[usage.time.length - 1]);
        var step = 60;
        var step_interpolation = everpolate.step;
        if (usage.mode === "sector") {
            while (m_end.diff(m_current, 'seconds') >= 0) {
                var enr_rate = step_interpolation(m_current, usage.time, usage.enr);
                m_current.add(step, 'seconds');
                var e_step_total = computation.p * (step / 3600);
                var e_step_enr = e_step_total * enr_rate;
                computation.push(moment(m_current), e_step_enr, e_step_total);
                battery.push(moment(m_current), 0, 0, battery.storage_enr[battery.storage_enr.length - 1] || battery.getChargeVoltage() * (battery.soc_enr * battery.q_rated), battery.storage_total[battery.storage_total.length - 1] || battery.getChargeVoltage() * (battery.soc * battery.q_rated), battery.soc_enr, battery.soc);
                sector.push(moment(m_current), e_step_enr, e_step_total);
            }

        }

        if (usage.mode === "battery") {

            while (m_end.diff(m_current, 'seconds') >= 0) {
                m_current.add(step, 'seconds');
                var q_current = battery.soc * battery.q_rated;
                var e_current = battery.getDischargeVoltage() * q_current;
                var q_step = computation.a_nom * (step / 3600);
                var e_step_total = computation.p * (step / 3600);
                var e_step_enr = e_step_total * battery.r_enr;
                var q_next = Math.max(q_current - q_step, battery.soc_min * battery.q_rated);
                battery.soc = Math.max(q_next / battery.q_rated, battery.soc_min);
                battery.soc_enr = battery.soc * battery.r_enr;
                var e_next = battery.getDischargeVoltage() * q_next;
                var e_enr_next = e_next * battery.r_enr;
                battery.push(moment(m_current), 0, 0, e_enr_next, e_next, battery.soc_enr, battery.soc);
                computation.push(moment(m_current), e_step_enr, e_step_total);
                sector.push(moment(m_current), 0, 0);
            }

        }

        if (usage.mode === "battery_sector") {

            while (m_end.diff(m_current, 'seconds') >= 0) {
                var enr_rate = step_interpolation(m_current, usage.time, usage.enr);
                m_current.add(step, 'seconds');
                var e_step_total1 = computation.p * (step / 3600);
                var e_step_enr1 = e_step_total1 * enr_rate;
                computation.push(moment(m_current), e_step_enr1, e_step_total1);

                var q_current = battery.soc * battery.q_rated;
                var v_current = battery.getChargeVoltage();
                var a_current = battery.a_nom;
                var v_max = battery.getChargeVoltageAt(battery.soc_max);

                if (v_current > battery.v_nom) {
                    var factor = (v_max - v_current) / (v_max - battery.v_nom);
                    var soc_factor = Math.min(Math.max(0.0, 1 - ((1 - battery.soc) / 0.25)), battery.soc_max);
                    var a_factor = a_current - (0.03 * battery.q_rated);
                    a_current = battery.a_nom - soc_factor * a_factor;

                }
                var e_current = v_current * q_current;
                var e_enr_current = e_current * battery.r_enr;

                if (v_current >= v_max) {
                    battery.push(moment(m_current), 0, 0, e_enr_current, e_current, battery.soc_enr, battery.soc);
                    sector.push(moment(m_current), e_step_enr1, e_step_total1);
                } else {
                    var q_step = a_current * (step / 3600);
                    var e_step_total = v_current * a_current * (step / 3600);
                    var e_step_enr = e_step_total * enr_rate;

                    // sector
                    var e_step_total2 = e_step_total;
                    var e_step_enr2 = e_step_enr;

                    var q_step = q_step * battery.battery_efficiency;
                    var e_step_total = e_step_total * battery.battery_efficiency;
                    var e_step_enr = e_step_enr * battery.battery_efficiency;

                    var q_next = q_current + q_step;
                    var soc_next = q_next / battery.q_rated;
                    battery.soc = soc_next;
                    battery.r_enr = (e_enr_current + e_step_enr) / (e_current + e_step_total);
                    battery.soc_enr = battery.soc * battery.r_enr;
                    var e_next = battery.getChargeVoltage() * q_next;
                    var e_next_enr = e_next * battery.r_enr;

                    battery.push(moment(m_current), e_step_enr, e_step_total, e_next_enr, e_next, battery.soc_enr, battery.soc);
                    sector.push(moment(m_current), e_step_enr1 + e_step_enr2, e_step_total1 + e_step_total2);
                }
            }
        }
    }

    function generateReference(json, format) {
        var parameters = new Parameters(json);
        var production = new Production(parameters);
        var usages = new Usages(parameters, production);
        var computation = new Computation(parameters);
        var battery = new Battery(parameters);
        var sector = new Sector(parameters);
        battery.init(usages.list[0].time[0]);
        computation.init(usages.list[0].time[0]);
        sector.init(usages.list[0].time[0]);
        for (let usage of usages.list) {
            usage.mode = "battery_sector";
            compute(usage, computation, battery, sector);
        }
        return new Practice('minimum',  parameters, production, battery, computation, sector);

    }

    function getAmperage(usage, battery, computation, sector){
        let coef_battery_diff = 1.;
        
        if (usage.mode === "sector") {
            coef_battery_diff = 1.;
        }

        if(usage.mode === 'battery'){
            do{
                // Create temporary clone of entities
                var tmpUsage = clone(usage)
                var tmpBattery = clone(battery)
                var tmpComputation = clone(computation)
                var tmpSector = clone(sector)

                // Apply coefficient to discharge and charge current
                tmpBattery.soc_max =  Math.max(tmpBattery.soc, usage.end_soc);
                tmpComputation.a_nom =  tmpComputation.a_nom * coef_battery_diff

                // Compute battery level
                var current_start_soc = tmpBattery.soc
                compute(tmpUsage, tmpComputation, tmpBattery, tmpSector)
                var current_end_soc = tmpBattery.soc
                var delta_soc = usage.end_soc - current_end_soc
                coef_battery_diff -= Math.sign(delta_soc) * RESOLUTION
                /*console.log("current : ", current_start_soc, ",",current_end_soc)
                console.log("target : ", usage.start_soc, ",",usage.end_soc)
                console.log("coeff : ", coef_battery_diff)*/
            } while ( delta_soc > RESOLUTION || delta_soc < -RESOLUTION);
        }
        if(usage.mode === 'battery_sector'){
            do{
                // Create temporary clone of entities
                var tmpUsage = clone(usage)
                var tmpBattery = clone(battery)
                var tmpComputation = clone(computation)
                var tmpSector = clone(sector)

                // Apply coefficient to discharge and charge current
                tmpBattery.soc_max =  Math.max(tmpBattery.soc, usage.end_soc);
                tmpBattery.a_nom =  tmpBattery.a_nom * coef_battery_diff

                // Compute battery level
                var current_start_soc = tmpBattery.soc
                compute(tmpUsage, tmpComputation, tmpBattery, tmpSector)
                var current_end_soc = tmpBattery.soc
                var delta_soc = usage.end_soc - current_end_soc
                coef_battery_diff += Math.sign(delta_soc) * RESOLUTION
                /*console.log("current : ", current_start_soc, ",",current_end_soc)
                console.log("target : ", usage.start_soc, ",",usage.end_soc)
                console.log("coeff : ", coef_battery_diff)*/
            } while ( delta_soc > RESOLUTION || delta_soc < -RESOLUTION);
        }
     return coef_battery_diff;
    }

    
    /**
     * Get the indexes of the variations for the given time series
     * @param {*} usages 
     */
    function getIndexesVariations(usages){
        var variations = [0];
        for(var i=1; i<usages.length-1; i++){
        prev_production = usages[i-1]
        curr_production = usages[i]
        next_production = usages[i+1]
        if (prev_production > curr_production && next_production > curr_production){
            variations.push(i)
        }
        else if(prev_production > curr_production && next_production == curr_production) {
            var j = i + 1;
            while(j < usages.length-1 && next_production == curr_production){
            curr_production = usages[j]
            next_production = usages[j+1]
            j += 1;
            }
            if(j<usages.length-1 && next_production > curr_production) {
            variations.push(i);
            }
        }       
        }
        variations.push(usages.length-1);
        return variations;
    }

    function computeBestUsages(parameters,  batteryAnom, computationAnom){
        var bestUsagesList = []

        var production = new Production(parameters);
        var indexesVariation = getIndexesVariations(production.enr);
        var startSoc = parameters.soc/100;
        var endSoc = startSoc;
        for(var i=0; i<indexesVariation.length-1; i++){
            // get variation peak
            var variation = production.enr.filter((production, j) => (indexesVariation[i] <= j  && j <= indexesVariation[i+1]));
            var argpeakVariation = variation.indexOf(Math.max(...variation));
            // discharge phase
            var startTimeDischarge = moment(production.time[indexesVariation[i]]);
            var endTimeDischarge = moment(production.time[indexesVariation[i] + argpeakVariation]).subtract(1, 'minutes');
            if(endTimeDischarge.isSameOrBefore(startTimeDischarge)) continue;

            var durationDischarge = endTimeDischarge.diff(startTimeDischarge, 'minutes');
            var durationFullDischarge = getTimeForFullDischarge(parameters, computationAnom, startSoc);
            
            
            if(durationFullDischarge > durationDischarge){
                var usage = '';
                //console.log('Discharge start at ', startTimeDischarge, '(',startSoc,'%)');
                usage += startTimeDischarge.format('kk:mm') + ',' + (startSoc*100) + ',';
                startSoc = getSocAfterDischargeDuration(parameters, startSoc, computationAnom, durationDischarge);;
                //console.log('Discharge end at ', endTimeDischarge, '(',startSoc,'%)');
                usage += endTimeDischarge.format('kk:mm') + ',' + (startSoc*100) + ', battery';
                bestUsagesList.push(usage);
               
            } else {
                var usage = '';
                //console.log('Discharge start at ', startTimeDischarge, '(',startSoc,'%)');
                usage += startTimeDischarge.format('kk:mm') + ',' + (startSoc*100) + ',';
                endTimeDischarge = moment(production.time[indexesVariation[i] + durationFullDischarge]).subtract(1, 'minutes');
                startSoc = getSocAfterDischargeDuration(parameters, startSoc, computationAnom, durationFullDischarge);
                //console.log('Discharge end at ', endTimeDischarge, '(',startSoc,'%)');
                usage += endTimeDischarge.format('kk:mm') + ',' + (startSoc*100) + ', battery';
                bestUsagesList.push(usage);
                
                var usage = '';
                var startTimeSector = moment(production.time[indexesVariation[i] + durationFullDischarge]);
                //console.log('Sector start at ', startTimeSector, '(',startSoc,'%)');
                usage += startTimeSector.format('kk:mm') + ',' + (startSoc*100) + ',';
                var endTimeSector =  moment(production.time[indexesVariation[i] + argpeakVariation]).subtract(1, 'minutes');
                durationSector = endTimeSector.diff(startTimeSector,'minutes');
                startSoc = getSocAfterDischargeDuration(parameters, startSoc, computationAnom, durationSector);
                //console.log('Sector end at ', endTimeSector, '(',startSoc,'%)');
                usage += endTimeSector.format('kk:mm') + ',' + (startSoc*100) + ', sector';
                bestUsagesList.push(usage);
            }
            
            //charge phase
            var usage = '';
            var startTimeCharge = moment(production.time[indexesVariation[i] + argpeakVariation]);
            var endTimeCharge = moment(production.time[indexesVariation[i+1]]).subtract(1, 'minutes');
            if(endTimeCharge.isSameOrBefore(startTimeCharge)) continue;

            var durationCharge = endTimeCharge.diff(startTimeCharge, 'minutes');
            var durationFullCharge = getTimeForFullCharge(parameters, computationAnom, startSoc);
            //console.log('Charge start at ', startTimeCharge, '(',startSoc,'%)');
            usage += startTimeCharge.format('kk:mm') + ',' + (startSoc*100) + ',';
            startSoc = getSocAfterChargeDuration(parameters, startSoc, batteryAnom, durationCharge);
            //console.log('Charge end at ', endTimeCharge, '(',startSoc,'%)');
            usage += endTimeCharge.format('kk:mm') + ',' + (startSoc*100) + ', battery_sector';
            bestUsagesList.push(usage);
        }
        //console.log(bestUsagesList);
        return bestUsagesList;
    }

    function computePractice(parameters, production, usages, battery, computation, sector){
        battery.init(usages.list[0].time[0]);
        computation.init(usages.list[0].time[0]);
        sector.init(usages.list[0].time[0]);
        var defaultBatteryAnom = battery.a_nom ;
        var defaultComputationAnom = computation.a_nom ;
        var coeff = 1;
        var computationAnomList = [];
        var batteryAnomList =  [];

        for (let usage of usages.list) {
            computation.a_nom = defaultComputationAnom;
            battery.a_nom = defaultBatteryAnom;

            coeff = getAmperage(usage, battery, computation, sector)

            if(usage.mode === 'battery') {
                computation.a_nom =  defaultComputationAnom * coeff;
                computationAnomList.push(defaultComputationAnom * coeff);
            }
            if(usage.mode === 'battery_sector'){
                battery.a_nom =  defaultBatteryAnom * coeff
                batteryAnomList.push(defaultBatteryAnom * coeff);
            } 
            compute(usage, computation, battery, sector);
        }
        return {computationAnomList, batteryAnomList}
    }


    function adjust(json) {
        var format = wNumb({
            decimals: 2,
        });

        var parameters = new Parameters(json);
        var production = new Production(parameters);
        var usages = new Usages(parameters, production);
        
        // Compute current practice
        var usages = new Usages(parameters, production);
        var battery = new Battery(parameters);
        var computation = new Computation(parameters);
        var sector = new Sector(parameters);

        battery.init(usages.list[0].time[0]);
        computation.init(usages.list[0].time[0]);
        sector.init(usages.list[0].time[0]);
        var defaultBatteryAnom = battery.a_nom;
        var defaultComputationAnom = computation.a_nom;
        var coeff = 1;
        var computationAnomList = [];
        var batteryAnomList =  [];
    
        var usage = usages.list[0];
    
        computation.a_nom = defaultComputationAnom;
        battery.a_nom = defaultBatteryAnom;
        coeff = getAmperage(usage, battery, computation, sector)
        if(usage.mode === 'battery') {
            computation.a_nom =  defaultComputationAnom * coeff;
            computationAnomList.push(defaultComputationAnom * coeff);
        }
        if(usage.mode === 'battery_sector'){
            battery.a_nom =  defaultBatteryAnom * coeff
            batteryAnomList.push(defaultBatteryAnom * coeff);
        } 
        return {computationAnomList, batteryAnomList}
    }

    function run(json) {
        var format = wNumb({
            decimals: 2,
        });
        // var practice_ref = generateReference(json, format);
        var parameters = new Parameters(json);
        var production = new Production(parameters);

        // Compute current practice
        var usages = new Usages(parameters, production);
        var battery = new Battery(parameters);
        var computation = new Computation(parameters);
        var sector = new Sector(parameters);
        var practice_cur = new Practice('current', parameters, production, usages,  battery, computation, sector);
        return practice_cur;
    }
    
module.exports = {
    run: function (json) {
        return run(json)
      },
    adjust: function (json, startTime, startSoc, endTime, endSoc, mode) {
        return adjust(json, startTime, startSoc, endTime, endSoc, mode)
      }
}