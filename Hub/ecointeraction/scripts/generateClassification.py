#coding: utf-8
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'ecointeraction.settings'
#import django
#django.setup()
from classification.models import InteractiveSystem, Entity, Criterium, Characteristic
from django import db
import time

duration = 5

def run():
    #FigureEnergy = InteractiveSystem.objects.get(name="FigureEnergy");
    FigureEnergy=InteractiveSystem(name="FigureEnergy", reference="Costanza, E., Ramchurn, S. D., & Jennings, N. R. (2012, September). Understanding domestic energy consumption through interactive visualisation: a field study. In Proceedings of the 2012 ACM Conference on Ubiquitous Computing (pp. 216-225). ACM.", abstract="Motivated by the need to better manage energy demand in the home, in this paper we advocate the integration into Ubicomp systems of interactive energy consumption visualisations, that allow users to engage with and understand their consumption data, relating it to concrete activities in their life. To this end, we present the design, implementation, and evaluation of FigureEnergy, a novel interactive visualisation that allows users to annotate and manipulate a graphical representation of their own electricity consumption data, and therefore make sense of their past energy usage and understand when, how, and to what end, some amount of energy was used. To validate our design, we deployed FigureEnergy 'in the wild' -- 12 participants installed meters in their homes and used the system for a period of two weeks. The results suggest that the annotation approach is successful overall: by engaging with the data users started to relate energy consumption to activities rather than just to appliances. Moreover, they were able to discover that some appliances consume more than they expected, despite having had prior experience of using other electricity displays.")
    FigureEnergy.save()
    print(FigureEnergy)

    #NuageVert=InteractiveSystem.objects.get(name="Nuage Vert");
    NuageVert=InteractiveSystem(name="Nuage Vert", reference="Evans, H., Hansen, H., & Hagedorn, J. (2009). Artful media: Nuage vert. IEEE MultiMedia, 16(3).", abstract="Because technical issues were a major challenge, we will describe in some detail the technical implementation of Nuage Vert. The system consists primarily of a thermal-imaging infrared camera, a computer executing real-time image processing, and a laser beam with scanning system to project the outline onto the vapor. The thermal-imaging camera produces a well-defined image of the vapor plume against the night sky. In earlier iterations of the design, we considered using Light Detection and Ranging (Lidar) to produce a high-fidelity image of the smoke plume, but this proved impossible due to the system's slow refresh rate of five minutes per frame.")
    NuageVert.save()
    print(NuageVert)

    #FlowerLamp=InteractiveSystem.objects.get(name="Flower Lamp");
    FlowerLamp=InteractiveSystem(name="Flower Lamp", reference="Backlund, S., Gyllenswärd, M., Gustafsson, A., Ilstedt Hjelm, S., Mazé, R., & Redström, J. (2007). Static! The aesthetics of energy in everyday things. In Proceedings of Design Research Society Wonderground International Conference 2006.", abstract="Static! is a project investigating interaction and product design as a way of increasing our awareness of how energy is used in everyday life. Revisiting the design of everyday things with focus on issues related to energy use, we have developed a palette of design examples in the form of prototypes, conceptual design proposals and use scenarios, to be used as a basis for communication and discussion with users and designers. With respect to design research and practice, the aim has been to develop a more profound understanding of energy as material in design, including its expressive and aesthetic potential, thus locating issues related to energy use at the centre of the design process.")
    FlowerLamp.save()
    print(FlowerLamp)

    #EnergyPlant=InteractiveSystem.objects.get(name="Energy Plant");
    EnergyPlant=InteractiveSystem(name="Energy Plant", reference="Loove Broms. 2011. Sustainable Interactions: Studies in the Design of Energy Awareness Artefacts. Licenciate thesis. Department of Computer and Information Science, Linköping University, Sweden. (April 2011).", abstract="The Energy Plant is an ambient transparent LCD-display that shows the electricity consumption of the household in the form of a growing plant. Each new month, a digital seed is 'planted' and starts to grow on the screen. Modest electricity consumption result in a thriving fast-growing plant and heavy consumption makes the plant wither. Taking care of the Energy Plant means reflecting on your electricity consumption and associating it with the excitement of seeing how the plant will evolve and grow.")
    EnergyPlant.save()
    print(EnergyPlant)

    #EnergyTree=InteractiveSystem.objects.get(name="Energy Tree");
    EnergyTree=InteractiveSystem(name="Energy Tree", reference="Piccolo, L. S., Baranauskas, C., & Azevedo, R. (2016). A socially inspired energy feedback technology: challenges in a developing scenario. AI & SOCIETY, 1-17.", abstract="Raising awareness of the environmental impact of energy generation and consumption has been a recent concern of contemporary society worldwide. Underlying the awareness of energy consumption is an intricate network of perception and social interaction that can be mediated by technology. In this paper we argue that issues regarding energy, environment and technology are very much situated and involve tensions of sociocultural nature. This exploratory investigation addresses the subject by introducing the design of a Socially-inspired Energy Eco-Feedback Technology (SEET), which is composed of an interactive system to trigger and mediate collective savings and a tangible device as a public feedback. Results of an evaluation situated in the context of a school in a socially disadvantaged area in Brazil are discussed, shedding light on the sociocultural aspects related to the subject. The role of the SEET to motivate energy awareness collectively among the social group is assessed, as well as the design characteristics that contributed to that. Outcomes bring to light social aspects and dynamics that would hardly have been predicted, evidencing critical factors related to a socially inspired design approach in the energy awareness domain.")
    EnergyTree.save()
    print(EnergyTree)

    #EnergyAwareClock=InteractiveSystem.objects.get(name="Energy AWARE Clock");
    EnergyAwareClock=InteractiveSystem(name="Energy AWARE Clock", reference="Broms, L., Katzeff, C., Bång, M., Nyblom, Å., Hjelm, S. I., & Ehrnberger, K. (2010, August). Coffee maker patterns and the design of energy feedback artefacts. In Proceedings of the 8th ACM Conference on Designing Interactive Systems (pp. 93-102). ACM.", abstract="Smart electricity meters and home displays are being installed in people's homes with the assumption that households will make the necessary efforts to reduce their electricity consumption. However, present solutions do not sufficiently account for the social implications of design. There is a potential for greater savings if we can better understand how such designs affect behaviour. In this paper, we describe our design of an energy awareness artefact - the Energy AWARE Clock - and discuss it in relation to behavioural processes in the home. A user study is carried out to study the deployment of the prototype in real domestic contexts for three months. Results indicate that the Energy AWARE Clock played a significant role in drawing households' attention to their electricity use. It became a natural part of the household and conceptions of electricity became naturalized into informants' everyday language." )
    EnergyAwareClock.save()
    print(EnergyAwareClock)

    #RevealIt=InteractiveSystem.objects.get(name="Reveal-it!");
    RevealIt=InteractiveSystem(name="Reveal-it!", reference="Valkanova, N., Jorda, S., Tomitsch, M., & Vande Moere, A. (2013, April). Reveal-it!: the impact of a social visualization projection on public awareness and discourse. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 3461-3470). ACM.", abstract="Public displays and projections are becoming increasingly available in various informal urban settings. However, their potential impact on informing and engaging citizens on relevant issues has still been largely unexplored. In this paper, we show that visualizations displayed in public settings are able to increase social awareness and discourse by exposing underlying patterns in data that is submitted by citizens. We thus introduce the design and evaluation of Reveal-it!, a public, interactive projection that facilitates the comparison of the energy consumptions of individuals and communities. Our in-the-wild deployment in three distinct physical locations provided insights into: 1) how people responded to this form of display in different contexts; 2) how it influenced people's perception and discussion of individual and communal data; and 3) the implications for a public visualization as a tool for increasing awareness and discourse. We conclude by discussing emerging participant behaviors, as well as some challenges involved in facilitating a socially motivated crowd-sourced visualization in the public context.")
    RevealIt.save()
    print(RevealIt)

    #HandyFeedback=InteractiveSystem.objects.get(name="Handy Feedback");
    HandyFeedback=InteractiveSystem(name="Handy Feedback", reference="Weiss, M., Mattern, F., Graml, T., Staake, T., & Fleisch, E. (2009, November). Handy feedback: Connecting smart meters with mobile phones. In Proceedings of the 8th international conference on mobile and ubiquitous multimedia (p. 15). ACM.", abstract="Reducing their energy consumption has become an important objective for many people. Consumption transparency and timely feedback are essential to support those who want to adjust their behavior in order to conserve energy. In this work, we propose an interactive system that provides instantaneous feedback concerning the energy usage on household and device level. For that, we used and extended the capabilities of a smart electricity meter, built a web-based API to enable interoperability with other applications, and developed a mobile phone interface that allows users to monitor, control, and measure the consumption of single appliances. Our system illustrates a way how usage barriers can be lowered and how high user involvement can be created. By providing users the electricity feedback needed -- in real-time and on device level -- the system allows for identifying the biggest energy guzzlers and helps users decrease their energy consumption.")
    HandyFeedback.save()
    print(HandyFeedback)

    #PowerAdvisor=InteractiveSystem.objects.get(name="PowerAdvisor");
    PowerAdvisor=InteractiveSystem(name="PowerAdvisor", reference="Kjeldskov, J., Skov, M. B., Paay, J., & Pathmanathan, R. (2012, May). Using mobile phones to support sustainability: a field study of residential electricity consumption. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 2347-2356). ACM.", abstract="Recent focus on sustainability has made consumers more aware of our joint responsibility for conserving energy resources such as electricity. However, reducing electricity use can be difficult with only a meter and a monthly or annual electricity bill. With the emergence of new power meters units, information on electricity consumption is now available digitally and wirelessly. This enables the design and deployment of a new class of persuasive systems giving consumers insight into their use of energy resources and means for reducing it. In this paper, we explore the design and use of one such system, Power Advisor, promoting electricity conservation through tailored information on a mobile phone or tablet. The use of the system in 10 households was studied over 7 weeks. Findings provide insight into peoples awareness of electricity consumption in their home and how this may be influenced through design.")
    PowerAdvisor.save()
    print(PowerAdvisor)

    #ForeWatch=InteractiveSystem.objects.get(name="FORE-Watch");
    ForeWatch=InteractiveSystem(name="FORE-Watch", reference="Schrammel, J., Gerdenitsch, C., Weiss, A., Kluckner, P. M., & Tscheligi, M. (2011, November). FORE-Watch–the clock that tells you when to use: persuading users to align their energy consumption with green power availability. In International Joint Conference on Ambient Intelligence (pp. 157-166). Springer Berlin Heidelberg.", abstract="Besides saving energy, using it at the right time (i.e. when there is a supply surplus, and the power is produced by sustainable power sources such as hydroelectricity or wind) is an important possibility to achieve positive effects for the environment. To enable the user to align their behavior with the dynamics of the energy generation they need to be informed about the current status of power supply and grid capacity. Furthermore, to be able to plan their behavior and possibly delay or advance consumption activities to more proper moments they also need to have access to high-quality forecasts about the future status of green energy supply. In this paper we present an ambient display design solution based on a common watch that is optimized for providing this information in an unobtrusive, ambient and persuasive way. We present and discuss requirements identified by use of literature analysis, focus groups and end-user questionnaires, outline approaches to calculate basic power generation forecasts based on weather forecast data and present an ambient interface concept designed to meet the identified requirements. We conclude that the developed approach has high potential to support desired behavior changes, and that achieving acceptable accuracy levels for the generation forecast is feasible with relatively little effort.")
    ForeWatch.save()
    print(ForeWatch)

    #PersonalizedEcoFeedback=InteractiveSystem.objects.get(name="Personalized Eco-feedback");
    PersonalizedEcoFeedback=InteractiveSystem(name="Personalized Eco-feedback", reference="Petkov, P., Goswami, S., Köbler, F., & Krcmar, H. (2012, October). Personalised eco-feedback as a design technique for motivating energy saving behaviour at home. In Proceedings of the 7th Nordic Conference on Human-Computer Interaction: Making Sense Through Design (pp. 587-596). ACM.", abstract="In recent years, interaction designers have actively started addressing sustainability as a research topic. More specifically, persuasive applications, which aim at promoting pro-environmental behaviour, such as energy saving have been of growing interest in multiple research disciplines. Driven by the proliferation of smart meters and energy monitors as well as the rise of social media, researchers and designers of persuasive applications have developed a wide range of design solutions that address this issue. The majority of them, however, provide the same information to users irrespective of differences in their environmental concerns and different motivations to conserve energy. Our research addresses this gap. We design mock-up screens that provide feedback catering towards different pro-environmental values and concerns and ask users to evaluate them in a survey setting. The research aims at understanding what feedback different people find relevant and therefore attempts to bridge the gap between environmental psychology and HCI. At the same time it provides insights for the design of personalised eco-feedback related to energy consumption.")
    PersonalizedEcoFeedback.save()
    print(PersonalizedEcoFeedback)

    #LimitEcoFeedback=InteractiveSystem.objects.get(name="Limit Eco-feedback");
    LimitEcoFeedback=InteractiveSystem(name="Limit Eco-feedback", reference="Pereira, L., Quintal, F., Barreto, M., & Nunes, N. J. (2013). Understanding the limitations of eco-feedback: a one-year long-term study. In Human-Computer Interaction and Knowledge Discovery in Complex, Unstructured, Big Data (pp. 237-255). Springer Berlin Heidelberg.", abstract="For the last couple of decades the world has been witnessing a change in habits of energy consumption in domestic environments, with electricity emerging as the main source of energy consumed. The effects of these changes in our eco-system are hard to assess, therefore encouraging researchers from different fields to conduct studies with the goal of understanding and improving perceptions and behaviors regarding household energy consumption. While several of these studies report success in increasing awareness, most of them are limited to short periods of time, thus resulting in a reduced knowledge of how householders will behave in the long-term. In this paper we attempt to reduce this gap presenting a long-term study on household electricity consumption. We deployed a real-time non-intrusive energy monitoring and eco-feedback system in 12 families during 52 weeks. Results show an increased awareness regarding electricity consumption despite a significant decrease in interactions with the eco-feedback system over time. We conclude that after one year of deployment of eco-feedback it was not possible to see any significant increase or decrease in the household consumption. Our results also confirm that consumption is tightly coupled with independent variables like the household size and the income-level of the families.")
    LimitEcoFeedback.save()
    print(LimitEcoFeedback)

    #EnergyLife=InteractiveSystem.objects.get(name="EnergyLife");
    EnergyLife=InteractiveSystem(name="EnergyLife", reference="Gamberini, L., Spagnolli, A., Corradi, N., Jacucci, G., Tusa, G., Mikkola, T., ... & Hoggan, E. (2012, June). Tailoring feedback to users’ actions in a persuasive game for household electricity conservation. In International Conference on Persuasive Technology (pp. 100-111). Springer Berlin Heidelberg.", abstract="Recent work has begun to focus on the use of games as a platform for energy awareness and eco-feedback research. While technical advancements (wireless sensors, fingerprinting) make timely and tailored feedback an objective within easy reach, we argue that taking into account the users’ own personal consumption behavior and tailoring feedback accordingly is a key requirement and a harder challenge. We present a first attempt in this direction, EnergyLife, which is designed to support the users’ actions and embeds contextualized feedback triggered by specific actions of the user, called ‘smart advice’. We conclude by showing the results of a four-month trial with four households that returned promising results on the effectiveness and acceptance of this feature.")
    EnergyLife.save()
    print(EnergyLife)

    #AbstractAmbient=InteractiveSystem.objects.get(name="Abstract Ambient");
    AbstractAmbient=InteractiveSystem(name="Abstract Ambient", reference="Rodgers, J., & Bartram, L. (2011). Exploring ambient and artistic visualization for residential energy use feedback. IEEE transactions on visualization and computer graphics, 17(12), 2489-2497.", abstract="Providing effective feedback on resource consumption in the home is a key challenge of environmental conservation efforts. One promising approach for providing feedback about residential energy consumption is the use of ambient and artistic visualizations. Pervasive computing technologies enable the integration of such feedback into the home in the form of distributed point-of-consumption feedback devices to support decision-making in everyday activities. However, introducing these devices into the home requires sensitivity to the domestic context. In this paper we describe three abstract visualizations and suggest four design requirements that this type of device must meet to be effective: pragmatic, aesthetic, ambient, and ecological. We report on the findings from a mixed methods user study that explores the viability of using ambient and artistic feedback in the home based on these requirements. Our findings suggest that this approach is a viable way to provide resource use feedback and that both the aesthetics of the representation and the context of use are important elements that must be considered in this design space.")
    AbstractAmbient.save()
    print(AbstractAmbient)

    #PowerViz=InteractiveSystem.objects.get(name="PowerViz");
    PowerViz=InteractiveSystem(name="PowerViz", reference="Paay, J., Kjeldskov, J., Skov, M. B., Lund, D., Madsen, T., & Nielsen, M. (2014, December). Design of an appliance level eco-feedback display for domestic electricity consumption. In Proceedings of the 26th Australian Computer-Human Interaction Conference on Designing Futures: the Future of Design (pp. 332-341). ACM.", abstract="Over the past decade there has been an increased focus on eco-feedback systems for electricity consumption due to emerging technologies that allow detailed and real-time usage data to be collected and presented to users. In this paper, we present the design of an always-on eco-feedback display, PowerViz, that provides information about people's power usage in their homes at an appliance level. In our study, we found that PowerViz increased awareness towards energy consumption, gave householders a better understanding of high consumption devices and made it easy for them to isolate and respond to unnecessary or 'greedy' appliances by turning them off or changing their use patterns. We also found that an ambient display of the household's total current electricity use both informed and attracted people to use the system when power usage became unusually high.")
    PowerViz.save()
    print(PowerViz)

    #EnergyLocalLamp=InteractiveSystem.objects.get(name="Energy Local Lamp");
    EnergyLocalLamp=InteractiveSystem(name="Energy Local Lamp", reference="Pierce, J., & Paulos, E. (2010, August). Materializing energy. In Proceedings of the 8th ACM Conference on Designing Interactive Systems (pp. 113-122). ACM.", abstract="Motivated and informed by perspectives on sustainability and design, this paper draws on a diverse body of scholarly works related to energy and materiality to articulate a perspective on energy-as-materiality and propose a design approach of materializing energy. Three critical themes are presented: the intangibility of energy, the undifferentiatedness of energy, and the availability of energy. Each theme is developed through combination of critical investigation and design exploration, including the development and deployment of several novel design artifacts: Energy Mementos and The Local Energy Lamp. A framework for interacting with energy-as-materiality is proposed involving collecting, keeping, sharing, and activating energy. A number of additional concepts are also introduced, such as energy attachment, energy engagement, energy attunement, local energy and energy meta-data. Our work contributes both a broader, more integrative design perspective on energy and materiality as well as a diversity of more specific concepts and artifacts that may be of service to designers and researchers of interactive systems concerned with sustainability and energy.")
    EnergyLocalLamp.save()
    print(EnergyLocalLamp)

    #EnergyDub=InteractiveSystem.objects.get(name="EnergyDub");
    EnergyDub=InteractiveSystem(name="EnergyDub", reference="Erickson, T., Li, M., Kim, Y., Deshpande, A., Sahu, S., Chao, T., ... & Naphade, M. (2013, April). The dubuque electricity portal: evaluation of a city-scale residential electricity consumption feedback system. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1203-1212). ACM.", abstract="This paper describes the Dubuque Electricity Portal, a city-scale system aimed at supporting voluntary reductions of electricity consumption. The Portal provided each household with fine-grained feedback on its electricity use, as well as using incentives, comparisons, and goal setting to encourage conservation. Logs, a survey and interviews were used to evaluate the user experience of the Portal during a 20-week pilot with 765 volunteer households. Although the volunteers had already made a wide range of changes to conserve electricity prior to the pilot, those who used the Portal decreased their electricity use by about 3.7%. They also reported increased understanding of their usage, and reported taking an array of actions - both changing their behavior and their electricity infrastructure. The paper discusses the experience of the system's users, and describes challenges for the design of ECF systems, including balancing accessibility and security, a preference for time-based visualizations, and the advisability of multiple modes of feedback, incentives and information presentation.")
    EnergyDub.save()
    print(EnergyDub)

    #Hems=InteractiveSystem.objects.get(name="HEMS");
    Hems=InteractiveSystem(name="HEMS", reference="Schwartz, T., Denef, S., Stevens, G., Ramirez, L., & Wulf, V. (2013, April). Cultivating energy literacy: results from a longitudinal living lab study of a home energy management system. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1193-1202). ACM.", abstract="This paper presents results of a three-year research project focused on the emplacement of Home Energy Management Systems (HEMS) in a living lab setting with seven households. The HEMS used in this study allowed householders to monitor energy consumption both in real-time and in retrospective on the TV and on mobile devices. Contrasting with existing research focused on how technology persuades people to consume less energy, our study uses a grounded approach to analyze HEMS emplacement. As an important result, we present here the issue of 'energy literacy'. Our study reveals that, by using HEMS, participants became increasingly literate in understanding domestic electricity consumption. We discuss the role HEMS played in that process and how the acquired literacy changed energy consumption patterns. We conclude that literacy in energy consumption has value on its own and explain how eco feedback system designs can benefit from this understanding.")
    Hems.save()
    print(Hems)

    #EnergyOrb=InteractiveSystem.objects.get(name="Energy Orb");
    EnergyOrb=InteractiveSystem(name="Energy Orb", reference="Faruqui, A., Sergici, S., & Sharif, A. (2010). The impact of informational feedback on energy consumption—A survey of the experimental evidence. Energy, 35(4), 1598-1608.", abstract="In theory, In-Home Displays (IHDs) can revolutionize the way utilities communicate information to customers because they can induce changes in customer behavior even when they are not accompanied by a change in electric prices or rebates for purchasing efficient equipment. IHDs provide consumers with direct feedback—real-time information on energy consumption and costs—and turn a once opaque and static electric bill into a transparent, dynamic, and controllable process. However, to what extent do consumers actually respond to the direct feedback provided by IHDs? In this paper, we seek to empirically answer this question by reviewing a dozen utility pilot programs in North America and abroad that focus on the energy conservation impact of IHDs. We also review overall customer opinions and attitudes towards IHDs and direct feedback to the extent that this information is available from the pilot studies. Our review indicates that the direct feedback provided by IHDs encourages consumers to make more efficient use of energy. We find that consumers who actively use an IHD can reduce their consumption of electricity on average by about 7 percent when prepayment of electricity is not involved. When consumers both use an IHD and are on an electricity prepayment system, they can reduce their electricity consumption by about twice that amount. In regard to demand response impacts, we find that the impact of time-of-use rates is augmented by direct feedback from IHDs.")
    EnergyOrb.save()
    print(EnergyOrb)

    #WattsWatt=InteractiveSystem.objects.get(name="Watt's Watt");
    WattsWatt=InteractiveSystem(name="Watt's Watt", reference="Jain, R. K., Taylor, J. E., & Peschiera, G. (2012). Assessing eco-feedback interface usage and design to drive energy efficiency in buildings. Energy and buildings, 48, 8-17. ISO 690", abstract="In response to growing concerns over climate change and rising energy costs, a number of eco-feedback systems are being tested by researchers. Yet, the interface design aspect of these systems has largely been ignored. Therefore, the role that interface design plays at the component level in driving actual energy savings from users is unclear. In this paper, we evaluate the impact interface design has on eco-feedback performance by investigating five established design components. We conducted a six week empirical study with 43 participants using a prototype eco-feedback interface. Analysis of usage data affirmed a statistically significant inverse correlation between user engagement (measured as logins) and energy consumption. Utilizing this relationship as a basis for performance, we expanded our analysis to evaluate the five design components. The study revealed statistically significant evidence corroborating that historical comparison and incentives are design components that drive higher engagement and thus reductions in energy consumption. Results for the normative comparison and disaggregation components were inconclusive, while results for the rewards and penalization component suggest that a revision to the penalization aspect of the component may be necessary. This study raises pertinent questions regarding the efficacy of various eco-feedback components in eliciting energy savings.")
    WattsWatt.save()
    print(WattsWatt)

    #EnergyWiz=InteractiveSystem.objects.get(name="EnergyWiz");
    EnergyWiz=InteractiveSystem(name="EnergyWiz", reference="Petkov, P., Köbler, F., Foth, M., & Krcmar, H. (2011, June). Motivating domestic energy conservation through comparative, community-based feedback in mobile and social media. In Proceedings of the 5th International Conference on Communities and Technologies (pp. 21-30). ACM.", abstract="The progress of technology has led to the increased adoption of energy monitors among household energy consumers. While the monitors available on the market deliver real-time energy usage feedback to the consumer, the format of this data is usually unengaging and mundane. Moreover, it fails to address consumers with different motivations and needs to save and compare energy. This paper presents a study that seeks to provide initial indications for motivation-specific design of energy-related feedback. We focus on comparative feedback supported by a community of energy consumers. In particular, we examine eco-visualisations, temporal self-comparison, norm comparison, one-on-one comparison and ranking, whereby the last three allow us to explore the potential of socialising energy-related feedback. These feedback types were integrated in EnergyWiz -- a mobile application that enables users to compare with their past performance, neighbours, contacts from social networking sites and other EnergyWiz users. The application was evaluated in personal, semi-structured interviews, which provided first insights on how to design motivation-related comparative feedback.")
    EnergyWiz.save()
    print(EnergyWiz)

    #WattLite=InteractiveSystem.objects.get(name="Watt-Lite");
    WattLite=InteractiveSystem(name="Watt-Lite", reference="Jönsson, L., Broms, L., & Katzeff, C. (2010, August). Watt-Lite: energy statistics made tangible. In Proceedings of the 8th ACM Conference on Designing Interactive Systems (pp. 240-243). ACM.", abstract="Increasing our knowledge of how design affects behaviour in the workplace has a large potential for reducing electricity consumption. This would be beneficial for the environment as well as for industry and society at large. In Western society energy use is hidden and for the great mass of consumers its consequences are poorly understood. In order to better understand how we can use design to increase awareness of electricity consumption in everyday life, we will discuss the design of Watt-Lite, a set of three oversized torches projecting real time energy statistics of a factory in the physical environments of its employees. The design of Watt-Lite is meant to explore ways of representing, understanding and interacting with electricity in industrial workspaces. We discuss three design inquiries and their implications for the design of Watt-Lite: the use of tangible statistics; exploratory interaction and transferred connotations.")
    WattLite.save()
    print(WattLite)

    #CustomisableDashboard=InteractiveSystem.objects.get(name="Customisable Dashboard");
    CustomisableDashboard=InteractiveSystem(name="Customisable Dashboard", reference="Filonik, D., Medland, R., Foth, M., & Rittenbruch, M. (2013, April). A customisable dashboard display for environmental performance visualisations. In International Conference on Persuasive Technology (pp. 51-62). Springer Berlin Heidelberg.", abstract="We conducted an exploratory study of a mobile energy monitoring tool: The Dashboard. Our point of departure from prior work was the emphasis of end-user customisation and social sharing. Applying extensive feedback, we deployed the Dashboard in real-world conditions to socially linked research participants for a period of five weeks. Participants were encouraged to devise, construct, place, and view various data feeds . The aim of our study was to test the assumption that participants, having control over their Dashboard configuration, would engage, and remain engaged, with their energy feedback throughout the trial. Our research points to a set of design issues surrounding the adoption and continued use of such tools. A novel finding of our study is the impact of social links between participants and their continued engagement with the Dashboard. Our results also illustrate the emergence of energy-voyeurism, a form of social energy monitoring by peers.")
    CustomisableDashboard.save()
    print(CustomisableDashboard)

    #TireeEnergyPulse=InteractiveSystem.objects.get(name="Tiree Energy Pulse");
    TireeEnergyPulse=InteractiveSystem(name="Tiree Energy Pulse", reference="Simm, W., Ferrario, M. A., Friday, A., Newman, P., Forshaw, S., Hazas, M., & Dix, A. (2015, April). Tiree energy pulse: exploring renewable energy forecasts on the edge of the grid. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (pp. 1965-1974). ACM.", abstract="In many parts of the world, the electricity supply industry makes the task of dealing with unpredictable spikes and dips in production and demand invisible to consumers, maintaining a seemingly unlimited supply. A future increase in reliance on time-variable renewable sources of electricity may lead to greater fluctuations in supply. We engaged remote islanders as equal partners in a research project that investigated through technology-mediated enquiry the topic of synchronising energy consumption with supply, and together built a prototype renewable energy forecast display. A number of participants described a change in their practices, saving high energy tasks for times when local renewable energy was expected to be available, despite having no financial incentive to do so. The main contributions of this paper are in: 1) the results of co-development sessions exploring systems supporting synchronising consumption with supply and 2) the findings arising from the deployment of the prototype.")
    TireeEnergyPulse.save()
    print(TireeEnergyPulse)

    #ConversationWashMachine=InteractiveSystem.objects.get(name="Conversation WashMachine");
    ConversationWashMachine=InteractiveSystem(name="Conversation WashMachine", reference="Bourgeois, J., Van Der Linden, J., Kortuem, G., Price, B. A., & Rimmer, C. (2014, September). Conversations with my washing machine: an in-the-wild study of demand shifting with self-generated energy. In Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing (pp. 459-470). ACM.",abstract="Domestic microgeneration is the onsite generation of low- and zero-carbon heat and electricity by private households to meet their own needs. In this paper we explore how an everyday household routine -- that of doing laundry -- can be augmented by digital technologies to help households with photovoltaic solar energy generation to make better use of self-generated energy. This paper presents an 8-month in-the-wild study that involved 18 UK households in longitudinal energy data collection, prototype deployment and participatory data analysis. Through a series of technology interventions mixing energy feedback, proactive suggestions and direct control the study uncovered opportunities, potential rewards and barriers for families to shift energy consuming household activities and highlights how digital technology can act as mediator between household laundry routines and energy demand-shifting behaviors. Finally, the study provides insights into how a 'smart' energy-aware washing machine shapes organization of domestic life and how people 'communicate' with their washing machine.")
    ConversationWashMachine.save()
    print(ConversationWashMachine)

    #LocalEnergyIndicator=InteractiveSystem.objects.get(name="Local Energy Indicator");
    LocalEnergyIndicator=InteractiveSystem(name="Local Energy Indicator", reference="Pierce, J., & Paulos, E. (2012, June). The local energy indicator: designing for wind and solar energy systems in the home. In Proceedings of the Designing Interactive Systems Conference (pp. 631-634). ACM.", abstract="This paper proposes and investigates the area of local energy for interactive systems design. We characterize local energy in terms of three themes: contextuality, seasonality, and visibility/tangibility. Here we focus on two specific local energy technologies domestic, electrical generation from wind and solar. In order to investigate this area we design, deploy and study a novel local energy device: The Local Energy Indicator. We conclude by outlining directions for future work related to local energy for interactive design.")
    LocalEnergyIndicator.save()
    print(LocalEnergyIndicator)

    #AgentB=InteractiveSystem.objects.get(name="AgentB");
    AgentB=InteractiveSystem(name="AgentB", reference="Costanza, E., Fischer, J. E., Colley, J. A., Rodden, T., Ramchurn, S. D., & Jennings, N. R. (2014, April). Doing the laundry with agents: a field trial of a future smart energy system in the home. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 813-822). ACM.", abstract="Future energy systems that rely on renewable energy may bring about a radical shift in how we use energy in our homes. We developed and prototyped a future scenario with highly variable, real-time electricity prices due to a grid that mainly relies on renewables. We designed and deployed an agent-based interactive system that enables users to effectively operate the washing machine in this scenario. The system is used to book timeslots of washing machine use so that the agent can help to minimize the cost of a wash by charging a battery at times when electricity is cheap. We carried out a deployment in 10 households in order to uncover the socio-technical challenges around integrating new technologies into everyday routines. The findings reveal tensions that arise when deploying a rationalistic system to manage contingently and socially organized domestic practices. We discuss the trade-offs between utility and convenience inherent in smart grid applications; and illustrate how certain design choices position applications along this spectrum.")
    AgentB.save()
    print(AgentB)

    #PowerAwareCord=InteractiveSystem.objects.get(name="Power-Aware Cord");
    PowerAwareCord=InteractiveSystem(name="Power-Aware Cord", reference="Gustafsson, A., & Gyllenswärd, M. (2005, April). The power-aware cord: energy awareness through ambient information display. In CHI'05 extended abstracts on Human factors in computing systems (pp. 1423-1426). ACM.", abstract="In order to support increased consumer awareness regarding energy consumption, we have been developing new ways of representing and interacting with energy in electric products intended for domestic environments. The 'Power-Aware Cord' is a re-design of a common electrical power strip that displays the amount of energy passing through it at any given moment. This is done by dynamic glowing patterns produced by electroluminescent wires molded into the transparent electrical cord. Using this fully functional prototype, we have been investigating how such ambient displays can be used to increase energy awareness. An initial user study indicates that the Power-Aware Cord is a very accessible and intuitive mean for better understanding energy consumption. Future work includes further development of the mapping between load and visual pattern and in-depth studies of user perception and learning over time.")
    PowerAwareCord.save()
    print(PowerAwareCord)

    #ShareAwareLight=InteractiveSystem.objects.get(name="Share AWARE Light");
    ShareAwareLight=InteractiveSystem(name="Share AWARE Light", reference="Loove Broms. 2011. Sustainable Interactions: Studies in the Design of Energy Awareness Artefacts. Licenciate thesis. Department of Computer and Information Science, Linköping University, Sweden. (April 2011).", abstract="The Share AWARE Light can be said to be situated at the other end of the spectrum with regard to the AWARE Puzzle Switch and the AWARE Handle. The Share Aware Light also employs the medium of light but, as the name implies, through a mutual, ongoing negotiation of sharing – making it something much more situated and conscious. Concretely, the Share AWARE Light is a series of portable, radio controlled light sources that share a fixed amount of light. For example, when one lamp is made brighter, the others lamps are proportionately dimmed by an equal amount. Light is used where it is needed the most, and where that might be is up for debate among its owners. The central idea explored with Share AWARE Light is how something fundamentally quite unpractical, a limited amount of light that has could instead be used as a central property that helps constitute the overall mythology of the product. Building on this idea, we designed each lamp to be perceived as a small and limited character that communicates its own needs and resources. Having an organic form and sized to fit in your palm, the Share AWARE Light is portable and cord-free, running on re-chargeable batteries. It can be carried and placed closed to the user for reading, convenience, company or just to create an overall ambience in the room. ")
    ShareAwareLight.save()
    print(ShareAwareLight)

    #Wattson=InteractiveSystem.objects.get(name="Wattson");
    Wattson=InteractiveSystem(name="Wattson", reference="Foster, D., Lawson, S., Blythe, M., & Cairns, P. (2010, October). Wattsup?: motivating reductions in domestic energy consumption using social networks. In Proceedings of the 6th Nordic Conference on Human-Computer Interaction: Extending Boundaries (pp. 178-187). ACM.", abstract="This paper reports on the design, deployment and evaluation of 'Wattsup', an innovative application which displays live autonomously logged data from the Wattson energy monitor, allowing users to compare domestic energy consumption on Facebook. Discussions and sketches from a workshop with Facebook users were used to develop a final design implemented using the Facebook API. Wattson energy monitors and the Wattsup app were deployed and trialled in eight homes over an eighteen day period in two conditions. In the first condition participants could only access their personal energy data, whilst in the second they could access each others' data to make comparisons. A significant reduction in energy was observed in the socially enabled condition. Comments on discussion boards and semi-structured interviews with the participants indicated that the element of competition helped motivate energy savings. The paper argues that socially-mediated banter and competition made for a more enjoyable user experience.")
    Wattson.save()
    print(Wattson)

    #Tenere=InteractiveSystem.objects.get(name="Tenere");
    Tenere=InteractiveSystem(name="Tenere", reference="Kim, J. W., Kim, Y. K., & Nam, T. J. (2009, April). The ténéré: design for supporting energy conservation behaviors. In CHI'09 Extended Abstracts on Human Factors in Computing Systems (pp. 2643-2646). ACM.", abstract="We present the Ténéré, electric power extension cords, designed to support people's energy conservation behaviors. The focus of design solutions was to provide appropriate energy awareness information in meaningful and emotional ways while products are being used. A narrative of tree was used to indicate energy use. The Tree of Tenere was the most isolated tree in the world. The tree is dead now and replace by a tree-like sculpture. It symbolizes the environmental consequences of human activity. When users overuse electricity, the graphics of the tree is transformed to the sculpture. This interactive graphics on the product encourages sustainable behaviors. Users are expected to be impressed and change their energy behaviors. Also we verified narrative-embedding approach is considerable method for industrial design field.")
    Tenere.save()
    print(Tenere)

    #StationEnr=InteractiveSystem.objects.get(name="StationENR");
    StationEnr=InteractiveSystem(name="StationENR", reference="Rivière, G., & Kreckelbergh, S. (2012, October). La StationENR pour sensibiliser aux énergies renouvelables par la modélisation de micro-réseaux. In Ergo'IHM 12 (pp. 63-66).", abstract="Actions to sensibilize the population to renewable energies are more often limited to inform the persons. An effective tool would be to make production and consumption data accessible and understandable. We propose a tangible and tactile interface allowing the simplified modeling of a micro-grid. This article presents the conception of the first prototype.")
    StationEnr.save()
    print(StationEnr)

    #ePoint=InteractiveSystem.objects.get(name="E-point");
    ePoint=InteractiveSystem(name="E-point", reference="Monigatti, P., Apperley, M., & Rogers, B. (2010, May). Power and energy visualization for the micro-management of household electricity consumption. In Proceedings of the International Conference on Advanced Visual Interfaces (pp. 325-328). ACM.", abstract="The paper describes a pilot system for the detailed management of domestic electricity consumption aimed at minimizing demand peaks and consumer cost. Management decisions are made both interactively by consumers themselves, and where practical, automatically by computer. These decisions are based on realtime pricing and availability information, as well as current and historic usage data. The benefits of the energy strategies implied by such a system are elaborated, showing the potential for significant peak demand reduction and slowing of the need for growth in generation capacity. An overview is provided of the component technologies and interaction methods we have designed, but the paper focuses on the communication of real-time information to the consumer through a combination of specific and ambient visualizations. There is a need for both overview information (eg how much power is being used right now; how much energy have we used so far today; what does it cost?) and information at the point-of-use (is it OK to turn this dryer on now, or should I wait until later?). To assist the design of these visualizations, a survey is underway aimed at establishing people's understanding of power and energy concepts.")
    ePoint.save()
    print(ePoint)

    #PowerSocket=InteractiveSystem.objects.get(name="PowerSocket");
    PowerSocket=InteractiveSystem(name="PowerSocket", reference="Heller, F., & Borchers, J. (2011, May). PowerSocket: towards on-outlet power consumption visualization. In CHI'11 extended abstracts on human factors in computing systems (pp. 1981-1986). ACM.", abstract="Power consumption is measured in W and Wh, but what do these units mean? Water consumption can easily be understood, as we all know what a liter of water looks like. Common power meters, however, rely on the physical units or their translation to costs as display. We classified existing displays and ambient visualizations in a taxonomy that focuses on the characteristics of power consumption displays. We adapted representatives of the different categories of displays to an on-outlet display and compared these using a combination of soft- and hardware prototyping. Results indicate that ambient visualizations make it easier to understand power consumption.")
    PowerSocket.save()
    print(PowerSocket)

    #PullMeOutPowerCord=InteractiveSystem.objects.get(name="Pull-me-out Power Cord");
    PullMeOutPowerCord=InteractiveSystem(name="Pull-me-out Power Cord", reference="Sohn, M., Nam, T., & Lee, W. (2009, April). Designing with unconscious human behaviors for eco-friendly interaction. In CHI'09 Extended Abstracts on Human Factors in Computing Systems (pp. 2651-2654). ACM.", abstract="Eco-design has become a central research issue for interaction design, as emerging interactive products can create serious environmental impacts while products are being used. We investigate a design method and develop case studies for eco-friendly interaction. A main concept of the design method is to apply unconscious human behaviors in interaction design. Products designed with this method are expected to be used unconsciously by users with reduced environmental impacts. In this paper, we present a framework of design space matrix and initial case studies for the design method. For the framework, we identified the types of interaction behaviors causing environmental impacts and the attributes of unconscious human behaviors. Based on the framework, three design cases - a power cord, a trashcan and a speedometer of an automobile - were developed. The proposed framework and design cases can be used as a base of an advanced eco-friendly interaction design method.")
    PullMeOutPowerCord.save()
    print(PullMeOutPowerCord)

    #Coralog=InteractiveSystem.objects.get(name="Coralog");
    Coralog=InteractiveSystem(name="Coralog", reference="Kim, T., Hong, H., & Magerko, B. (2010, August). Design requirements for ambient display that supports sustainable lifestyle. In Proceedings of the 8th ACM Conference on Designing Interactive Systems (pp. 103-112). ACM.", abstract="People are ready to change themselves to adopt more eco-friendly habits such as conserving electricity when they are aware of the possible problems of their lifestyle. In this sense, ambient display, which users experience occasionally without its interfering with their primary tasks, is well suited to provide the feedback of their personal activities in a more subtle manner than direct information presentation. We present the results of user studies with two ambient displays in different visualization styles. Participants showed diverse usage behaviors of ambient displays according to their motivational level of sustainable lifestyle. In addition, iconic metaphor of eco-visualization can trigger more emotional attachment while indexical representation helps retrospective functions. Finally, we suggest design requirements for ambient displays that support different stages of persuasion from raising awareness to motivating to change behaviors and to maintaining desired habits.")
    Coralog.save()
    print(Coralog)

    #WattBot=InteractiveSystem.objects.get(name="WattBot");
    WattBot=InteractiveSystem(name="WattBot", reference="Petersen, D., Steele, J., & Wilkerson, J. (2009, April). WattBot: a residential electricity monitoring and feedback system. In CHI'09 Extended Abstracts on Human Factors in Computing Systems (pp. 2847-2852). ACM.", abstract="Electricity production emits carbon dioxide and other gases into the atmosphere, adversely influences global climate change, depletes limited natural resources, and negatively impacts the lives of those who live near power plants. We designed a residential electricity monitoring and feedback system called WattBot, that allows users to track their home energy usage and encourages them to reduce consumption. Our solution is an application for the Apple iPhone and iPod touch that receives data from a wireless hub, allowing users to view, compare and analyze their electricity usage over time.")
    WattBot.save()
    print(WattBot)

    #Flo=InteractiveSystem.objects.get(name="Flo");
    Flo=InteractiveSystem(name="Flo", reference="Shrubsole, P., Lavrysen, T., Janse, M., & Weda, H. (2011, May). Flo: raising family awareness about electricity use. In CHI'11 Extended Abstracts on Human Factors in Computing Systems (pp. 669-672). ACM.", abstract="In this case study, we designed a family game to explore whether this could be an effective and fun approach for raising the awareness of family members towards their energy use and, in the long run, to provide an effective tool for affecting their habits regarding sustainable behavior. The design of the family game implemented the metaphor of electricity as flowing liquid, fostered fun experiences and supported competitive and social elements. Dutch families with children, aged 5-11 years, participated in the design and evaluation of the concept. We obtained valuable insights into the use and understanding of electricity by the families, how the families looked at responsible behaviors around their usage and how a game could integrate into the family context in a fun way.")
    Flo.save()
    print(Flo)

    #StationaryEcd=InteractiveSystem.objects.get(name="Stationary ECD");
    StationaryEcd=InteractiveSystem(name="Stationary ECD", reference="Yun, T. J. (2009, April). Investigating the impact of a minimalist in-home energy consumption display. In CHI'09 Extended Abstracts on Human Factors in Computing Systems (pp. 4417-4422). ACM.", abstract="We investigated the impact of a minimal in-home Energy Consumption Display (ECD), both stationary and portable versions, on household energy awareness and consumption. We deployed the ECD in eight homes for three weeks each, providing half of the participants with a portable version and the others with a stationary one. This work presents an account of each user's experience through pre- and post-surveys, power meter data, and post-deployment interviews and results of the study, which show that users reduced energy consumption by identifying high-power devices in their home and by playfully setting conservation goals.")
    StationaryEcd.save()
    print(StationaryEcd)

    #MobileEcd=InteractiveSystem.objects.get(name="Mobile ECD");
    MobileEcd=InteractiveSystem(name="Mobile ECD", reference="Yun, T. J. (2009, April). Investigating the impact of a minimalist in-home energy consumption display. In CHI'09 Extended Abstracts on Human Factors in Computing Systems (pp. 4417-4422). ACM.", abstract="We investigated the impact of a minimal in-home Energy Consumption Display (ECD), both stationary and portable versions, on household energy awareness and consumption. We deployed the ECD in eight homes for three weeks each, providing half of the participants with a portable version and the others with a stationary one. This work presents an account of each user's experience through pre- and post-surveys, power meter data, and post-deployment interviews and results of the study, which show that users reduced energy consumption by identifying high-power devices in their home and by playfully setting conservation goals.")
    MobileEcd.save()
    print(MobileEcd)

    #LightningFeedbackDisplay=InteractiveSystem.objects.get(name="Lightning Feedback Display");
    LightningFeedbackDisplay=InteractiveSystem(name="Lightning Feedback Display", reference="Ham, J., & Midden, C. (2010, June). Ambient persuasive technology needs little cognitive effort: the differential effects of cognitive load on lighting feedback versus factual feedback. In International Conference on Persuasive Technology (pp. 132-142). Springer Berlin Heidelberg.",abstract="Persuasive technology can influence behavior or attitudes by for example providing interactive factual feedback about energy conservation. However, people often lack motivation or cognitive capacity to consciously process such relative complex information (e.g., numerical consumption feedback). Extending recent research that indicates that ambient persuasive technology can persuade the user without receiving the user’s conscious attention, we argue here that Ambient Persuasive Technology can be effective while needing only little cognitive resources, and in general can be more influential than more focal forms of persuasive technology. In an experimental study, some participants received energy consumption feedback by means of a light changing color (more green=lower energy consumption, vs. more red=higher energy consumption) and others by means of numbers indicating kWh consumption. Results indicated that ambient feedback led to more conservation than factual feedback. Also, as expected, only for participants processing factual feedback, additional cognitive load lead to slower processing of that feedback. This research sheds light on fundamental characteristics of Ambient Persuasive Technology and Persuasive Lighting, and suggests that it can have important advantages over more focal persuasive technologies without losing its persuasive potential.")
    LightningFeedbackDisplay.save()
    print(LightningFeedbackDisplay)

    #OaksAndCounting=InteractiveSystem.objects.get(name="7000 oaks and counting");
    OaksAndCounting=InteractiveSystem(name="7000 oaks and counting", reference="Holmes, T. G. (2007, June). Eco-visualization: combining art and technology to reduce energy consumption. In Proceedings of the 6th ACM SIGCHI conference on Creativity & cognition (pp. 153-162). ACM.", abstract="Can creative visualizations of real time energy consumption patterns trigger more ecologically responsible behavior? Media art that displays the real time usage of key resources such as electricity offers new strategies to conserve energy in the home and workplace. This paper details the development of a public art project created for the National Center for Supercomputing Applications that measures electricity usage in real time for the purpose of education and curtailment of power usage. A version of this piece will be on view in the exhibition, Speculative Data and the Creative Imaginary, a component of the 2007 Creativity and Cognition conference.")
    OaksAndCounting.save()
    print(OaksAndCounting)

    #Boel=InteractiveSystem.objects.get(name="BoEl");
    Boel=InteractiveSystem(name="BoEl", reference="Elin Engquist. 2009. BOEL-lampan: Utveckling av en lampa för visualisering av elförbrukning i hemmet. Master's thesis. Mälardalen University, Sweden. (June 2009)", abstract="BoEL is an experimental social ambient interface and web service that presents daily consumption figures to home owners and neighbours to promote joint savings and foster competitive energy saving behaviours. The service includes an ambient lamp that provides feedback on the energy consumption in the household and these interfaces are installed so that the neighbours can observe each others energy status. We have chosen to explore whether the local street can motivate people to reduce their electricity consumption. By using the local setting as a key element for the project we hope to make use of the stereotypical neighbourhood behaviour. One always wants to beat the neighbour by having the most well trimmed lawn, the best barbecue, the nicest car (hence the expression ‘keeping up with the Jones’). By using this competing element between neighbours/users we hope to trigger them to changed behaviour through peer pressure.")
    Boel.save()
    print(Boel)

    #TariffAgent=InteractiveSystem.objects.get(name="TariffAgent");
    TariffAgent=InteractiveSystem(name="TariffAgent", reference="Alan, A. T., Costanza, E., Ramchurn, S. D., Fischer, J., Rodden, T., & Jennings, N. R. (2016). Tariff agent: interacting with a future smart energy system at home. ACM Transactions on Computer-Human Interaction (TOCHI), 23(4), 25.", abstract="Smart systems are becoming increasingly ubiquitous and consequently transforming our lives. The level of system autonomy plays a vital role in the development of smart systems as it profoundly affects how people and these systems interact with each other. However, to date, there are very few studies on human interaction with such systems. This paper presents findings from two field studies where two different prototypes for automating energy tariff-switching were developed and evaluated in the wild. Both prototypes offer flexible autonomy by which users can shift the system's level of autonomy among three options: suggestion-only, semi-autonomy, and full autonomy, whenever they like. Our findings based on thematic analysis show that flexible autonomy is a promising way to sustain users' engagement with smart systems, despite their occasional mistakes. The findings also suggest that users take responsibility for the undesired outcomes of automated actions when delegation of autonomy can be adjusted flexibly.")
    TariffAgent.save()
    print(TariffAgent)

    #HeatDial=InteractiveSystem.objects.get(name="HeatDial");
    HeatDial=InteractiveSystem(name="HeatDial", reference="Jensen, R. H., Kjeldskov, J., & Skov, M. B. (2016, October). HeatDial: Beyond User Scheduling in Eco-Interaction. In Proceedings of the 9th Nordic Conference on Human-Computer Interaction (p. 74). ACM.", abstract="There has been an interesting development within sustainable HCI, from passive feedback-displays towards more interactive systems that allow users to schedule their energy usage for optimal times based on eco-feedback and eco-forecasting. In this paper, we extend previous work on user scheduling of energy usage in eco-interaction with a study of heat pump control in domestic households. Aiming at using electricity when it is either cheap or green, our approach is to provide users with an interface where they can set temperature boundaries for the home, and interactively evaluate the impact of different settings on predicted energy cost. Based on this input, the scheduling of energy use is done by an automated system monitoring temperatures and electricity prices. We conducted a qualitative study of the HeatDial prototype with 5 families over 6 months. Key findings were that HeatDial supported users identifying and acting on opportunities for reducing costs, but that automation also had an impact on user engagement and highlighted a need for more feedback on how the system intended to act.")
    HeatDial.save()
    print(HeatDial)

    #AgentSwitch=InteractiveSystem.objects.get(name="AgentSwitch");
    AgentSwitch=InteractiveSystem(name="AgentSwitch", reference="Fischer, J. E., Ramchurn, S. D., Osborne, M., Parson, O., Huynh, T. D., Alam, M., ... & Costanza, E. (2013, March). Recommending energy tariffs and load shifting based on smart household usage profiling. In Proceedings of the 2013 international conference on Intelligent user interfaces (pp. 383-394). ACM.", abstract="We present a system and study of personalized energy-related recommendation. AgentSwitch utilizes electricity usage data collected from users' households over a period of time to realize a range of smart energy-related recommendations on energy tariffs, load detection and usage shifting. The web service is driven by a third party real-time energy tariff API (uSwitch), an energy data store, a set of algorithms for usage prediction, and appliance-level load disaggregation. We present the system design and user evaluation consisting of interviews and interface walkthroughs. We recruited participants from a previous study during which three months of their household's energy use was recorded to evaluate personalized recommendations in AgentSwitch. Our contributions are a) a systems architecture for personalized energy services; and b) findings from the evaluation that reveal challenges in designing energy-related recommender systems. In response to the challenges we formulate design recommendations to mitigate barriers to switching tariffs, to incentivize load shifting, and to automate energy management.")
    AgentSwitch.save()
    print(AgentSwitch)

    #TemperatureCalendar=InteractiveSystem.objects.get(name="Temperature Calendar");
    TemperatureCalendar=InteractiveSystem(name="Temperature Calendar", reference="Costanza, E., Bedwell, B., Jewell, M. O., Colley, J., & Rodden, T. (2016, May). 'A bit like British Weather, I suppose': Design and Evaluation of the Temperature Calendar. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 4061-4072). ACM.", abstract="In this paper we present the design and evaluation of the Temperature Calendar -- a visualization of temperature variation within a workplace over the course of the past week. This highlights deviation from organizational temperature policy, and aims to bring staff 'into the loop' of understanding and managing heating, and so reduce energy waste. The display was deployed for three weeks in five public libraries. Analysis of interaction logs, questionnaires and interviews shows that staff used the displays to understand heating in their buildings, and took action reflecting this new understanding. Bringing together our results, we discuss design implications for workplace displays, and an analysis of carbon emissions generated in constructing and operating our design. More in general, the findings helped us to reflect on the role of policy on energy consumption, and the potential for the HCI community to engage with its application, as well as its definition or modification.")
    TemperatureCalendar.save()
    print(TemperatureCalendar)

    #Velix=InteractiveSystem.objects.get(name="Velix");
    Velix=InteractiveSystem(name="Velix", reference="Graml, T., Loock, C. M., Baeriswyl, M., & Staake, T. (2011, June). Improving residential energy consumption at large using persuasive systems. In ECIS.", abstract="The paper presents a persuasive web application that stimulates residential energy conservation. The users of the application received consumption feedback that is based on electricity meter readings which they entered over a period of 6 months and which accounted for specific household characteristics. In a large scale field study which we conducted between April and September of 2010, 6’921 participants used the application. From a research perspective, the system allowed us to experimentally assess the effects of different socio-psychological concepts with regard to different measures such as popularity, choice, and energy conservation. The large user base and the real-world setting contributed to the validity of the findings. The discussion presented is structured along a behavioural change framework we adapted from Ölander’s and J. Thøgersen’s motivation – ability – opportunity model. Besides presenting the quantitative results of multiple studies and providing theoretical cues to outline the mechanisms behind the behaviour, we formulate guidelines that support the development of similar applications in research and industry.")
    Velix.save()
    print(Velix)

    #EcoFeedback=InteractiveSystem.objects.get(name="EcoFeedback");
    EcoFeedback=InteractiveSystem(name="EcoFeedback", reference="Ma, G., Lin, J., Li, N., & Zhou, J. (2017). Cross-cultural assessment of the effectiveness of eco-feedback in building energy conservation. Energy and Buildings, 134, 329-338.", abstract="Ma, G., Lin, J., Li, N., & Zhou, J. (2017). Cross-cultural assessment of the effectiveness of eco-feedback in building energy conservation. Energy and Buildings, 134, 329-338.")
    EcoFeedback.save()
    print(EcoFeedback)

    #WATTSBurning=InteractiveSystem.objects.get(name="WATTSBurning");
    WATTSBurning=InteractiveSystem(name="WATTSBurning", reference="APA Quintal, F., Pereira, L., Nunes, N., Nisi, V., & Barreto, M. (2013, September). WATTSBurning: design and evaluation of an innovative eco-feedback system. In IFIP Conference on Human-Computer Interaction (pp. 453-470). Springer Berlin Heidelberg.", abstract="This paper reports a 15 weeks study of artistic eco-feedback deployed in six houses with an innovative sensing infrastructure and visualization strategy. The paper builds on previous work that showed a significant decrease in user awareness after a short period with a relapse in consumption. In this study we aimed to investigate if new forms of feedback could overcome this issue, maintaining the users awareness for longer periods of time. The study presented here aims at understanding if people are more aware of their energy consumption after the installation of a new, art inspired eco-feedback. The research question was then: does artistic eco-feedback provide an increased awareness over normal informative feedback? And does that awareness last longer? To answer this questions participants were interviewed and their consumption patterns analyzed. The main contribution of the paper is to advance our knowledge about the effectiveness of eco-feedback and provide guidelines for implementation of novel eco-feedback visualizations that overcome the relapse behavior pattern.")
    WATTSBurning.save()
    print(WATTSBurning)

    #IDO=InteractiveSystem.objects.get(name="ID-O");
    IDO=InteractiveSystem(name="ID-O", reference="Yun, R., Aziz, A., Scupelli, P., Lasternas, B., Zhang, C., & Loftness, V. (2015, April). Beyond eco-feedback: adding online manual and automated controls to promote workplace sustainability. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (pp. 1989-1992). ACM.", abstract="Whereas eco-feedback has been widely studied in HCI and environmental psychology, online manual control and automated control have been rarely studied with a focus on their long-term quantitative impact and usability. To address this, an intervention was tested with eighty office workers for twenty-seven weeks. Through the long-term field test, it was found that the addition of online controls in the feedback intervention led to more energy savings than feedback only and worked better for light and phone usage than computer and monitor usage. The addition of automated control led to the greatest savings but was less effective for efficient users than inefficient ones.")
    IDO.save()
    print(IDO)

    #MyLocalEnergy=InteractiveSystem.objects.get(name="MyLocalEnergy");
    MyLocalEnergy=InteractiveSystem(name="MyLocalEnergy", reference="Castelli, N., Stevens, G., Jakobi, T., & Schönau, N. (2016). Beyond Eco-feedback: Using Room as a Context to Design New Eco-support Features at Home. In Advances and New Trends in Environmental and Energy Informatics (pp. 177-195). Springer International Publishing.", abstract="In recent years research in Sustainable Interaction Design has put major efforts into understanding the potentials of saving energy in private households by providing energy consumption feedback. Trying to overcome pitfalls such as invisibility and immateriality, a great variety of designs with saving potentials from 5–15 %, has emerged. However, feedback mechanisms are mostly reduced to a one-dimensional view on motivating energy savings. In this paper, we argue to take a broader view on eco-support, where eco-feedback should be used in combination with eco-control and eco-automation features. All these features have in common that they aim to reduce energy consumption in practice. From such a holistic understanding of eco-support, we demonstrate how design could benefit from ubiquitous- and context-aware computing approaches to enrich feedback, increase control and automatize cumbersome and boring routines. We use the presence of a user on room level as context information. Rooms present an essential domestic ordering system that structures daily routines at home. In this paper, we show that the usage of room-as-a-context has fundamental implications for the design of domestic indoor localization concepts. In addition, we show how the different types of eco-support systems benefit from it. We illustrate our consideration by presenting a prototype for Android based tablets, which was used to study the design concepts in the wild.")
    MyLocalEnergy.save()
    print(MyLocalEnergy)

    #WattISee=InteractiveSystem.objects.get(name="Watt-I-See");
    WattISee=InteractiveSystem(name="Watt-I-See", reference="Quintal, F., Jorge, C., Nisi, V., & Nunes, N. (2016, June). Watt-I-See: A Tangible Visualization of Energy. In Proceedings of the International Working Conference on Advanced Visual Interfaces (pp. 120-127). ACM.", abstract="This paper describes a tangible visualization that explores the link between the impact of energy feedback on household consumers and the resource demand impact on energy production. Specifically, it positions a novel perspective attempting to move beyond the known limitations of current eco-feedback systems and contributes to enhance our understanding of how consumers comprehend energy production. The work is informed by a comprehensive study of an installation that displays the ratio of current power generation sources and the percentage of grid renewables. The paper provides design insights for creating novel eco-feedback visualizations that leverage the balance between user lifestyles and the desire to influence consumption behaviors and practices. Evaluation results show an increase in energy literacy and awareness as well as identifies high consumer preferences towards simple, representative interfaces and ubiquitous immediate feedback. Our study shows potential in terms of future scenarios for eco-feedback in distributed energy micro-generation and other inevitable disruptive changes for the energy utility.")
    WattISee.save()
    print(WattISee)

    #POEM=InteractiveSystem.objects.get(name="POEM");
    POEM=InteractiveSystem(name="POEM", reference="Milenkovic, M., Hanebutte, U., Huang, Y., Prendergast, D., & Pham, H. (2013, April). Improving user comfort and office energy efficiency with POEM (personal office energy monitor). In CHI'13 Extended Abstracts on Human Factors in Computing Systems (pp. 1455-1460). ACM.", abstract="Consensus exists in much of industry and academia that engaging end-users is an essential element for improving energy efficiency in office buildings. We present our experiences implementing and deploying POEM (Personal Office Energy Monitor) with real office users. POEM is an end-user eco-feedback application. It provides detailed personalized data on energy usage and ambient conditions to each office user, as well as reporting aggregates for building-level management and policy setting. The POEM UI also allows users to state their subjective feeling of comfort. The system aggregates those inputs and informs the building manager to take corrective action if needed - thus closing the control loop between the people and the building. We report our findings from pilot tests of POEM prototype.")
    POEM.save()
    print(POEM)

    #eForecast=InteractiveSystem.objects.get(name="eForecast");
    eForecast=InteractiveSystem(name="eForecast", reference="Kjeldskov, J., Skov, M. B., Paay, J., Lund, D., Madsen, T., & Nielsen, M. (2015, December). Facilitating Flexible Electricity Use in the Home with Eco-Feedback and Eco-Forecasting. In Proceedings of the Annual Meeting of the Australian Special Interest Group for Computer Human Interaction (pp. 388-396). ACM.", abstract="Over the last decade there has been an increased focus on changing domestic electricity consumption behaviors. While the usual approach has been to facilitate reduced consumption, recent work has started looking at facilitating more flexible electricity use as a means of shifting consumption to more favorable times. This approach means that people may behave more sustainably without necessarily using less electricity. Exploring this emerging approach, this paper presents a study of flexibility in domestic electricity use as facilitated by an eco-feedback system with forecast information about price, availability of green energy, and grid demand. The prototype system was deployed in three households for 22 weeks. Our findings show that flexible electricity use is far from trivial to achieve in domestic households. The details of this is relevant for understanding people's ability and willingness to shift electricity consumption, and for the design of systems that facilitate doing this.")
    eForecast.save()
    print(eForecast)

    #Ecosphere=InteractiveSystem.objects.get(name="Ecosphere");
    Ecosphere=InteractiveSystem(name="Ecosphere", reference="Snow, S., Vyas, D., & Brereton, M. (2015). When an eco-feedback system joins the family. Personal and Ubiquitous Computing, 19(5-6), 929-940.", abstract="The dynamic, chaotic, intimate and social nature of family life presents many challenges when designing interactive systems in the household space. This paper presents findings from a whole-of-family approach to studying the use of an energy awareness and management system called 'Ecosphere'. Using a novel methodology of inviting 12 families to create their own self-authored videos documenting their energy use, we report on the family dynamics and nuances of family life that shape and affect this use. Our findings suggest that the momentum of existing family dynamics in many cases obstructs behaviour change and renders some family members unaware of energy consumption despite the presence of an energy monitor display in the house. The implication for eco-feedback design is that it needs to recognise and respond to the kinds of family relations into which the system is embedded. In response, we suggest alternative ways of sharing energy-related information among families and incentivising engagement among teenagers.")
    Ecosphere.save()
    print(Ecosphere)

    #ArchiExpression=InteractiveSystem.objects.get(name="ArchiExpression");
    ArchiExpression=InteractiveSystem(name="ArchiExpression", reference="Liu, T., Ding, X., Liu, P., Lu, T., & Gu, N. (2016, May). ArchiExpression: A Physical Eco-Feedback Display in an Outdoor Campus Space of China. In Proceedings of the Fourth International Symposium on Chinese CHI (p. 5). ACM.", abstract="Eco-feedback is popularly explored as an approach to promoting energy conservation, usually examined in residential settings with screen-based displays. How a physical eco-feedback display may work in a non-residential setting, e.g. campus, is still relatively underexplored. This paper presents a physical eco-feedback display - ArchiExpression - to be installed in a shared outdoor space of China, and explores its role in engaging attention and awareness on energy related issues for people of the space. Rather than showing energy information visually and accurately on a screen-based display, ArchiExpression presents information physically and ambiguously with a matrix of solar panel units. A two-week study of its deployment in a university campus of China illustrates its effectiveness in engaging people's interests, as well as people's reflections on energy consumption and the meanings of the eco-feedback design itself. The study highlights how the context, the form and the ambiguity shape the meanings of the eco-feedback display and people's interactions with it.")
    ArchiExpression.save()
    print(ArchiExpression)

    #BizWatts=InteractiveSystem.objects.get(name="BizWatts");
    BizWatts=InteractiveSystem(name="BizWatts", reference="Gulbinas, R., Jain, R. K., & Taylor, J. E. (2014). BizWatts: A modular socio-technical energy management system for empowering commercial building occupants to conserve energy. Applied Energy, 136, 1076-1084.", abstract="Commercial buildings represent a significant portion of energy consumption and environmental emissions worldwide. To help mitigate the environmental impact of building operations, building energy management systems and behavior-based campaigns designed to reduce energy consumption are becoming increasingly popular. In this paper, we describe the development of a modular socio-technical energy management system, BizWatts, which combines the two approaches by providing real-time, appliance-level power management and socially contextualized energy consumption feedback. We describe in detail the physical and virtual architecture of the system, which simultaneously engages building occupants and facility managers, as well as the main principles behind the interface design and component functionalities. A discussion about how the data collection capabilities of the system enable insightful commercial building energy efficiency studies and quantitative network analysis is also included. We conclude by commenting on the validation of the system, identifying current system limitations and introducing new research avenues that the development and deployment of BizWatts enables.")
    BizWatts.save()
    print(BizWatts)

    #EcoAwareCoffeeMaker=InteractiveSystem.objects.get(name="Eco-Aware CoffeeMaker");
    EcoAwareCoffeeMaker=InteractiveSystem(name="Eco-Aware CoffeeMaker", reference="Casado-Mansilla, D., Lopez-de-Armentia, J., Garaizar, P., & López-de-Ipiña, D. (2014, April). To switch off the coffee-maker or not: that is the question to be energy-efficient at work. In CHI'14 Extended Abstracts on Human Factors in Computing Systems (pp. 2425-2430). ACM.", abstract="There are some barriers to reduce energy consumption in shared spaces where many people use common electronic devices (e.g. dilution of responsibility, the trade-off between comfort and necessity, absentmindedness, or the lack of support to foster energy-efficiency). The workplace is a challenging scenario since the economic incentives are not present to increase energy awareness. To tackle some of these issues we have augmented a shared coffee-maker with eco-feedback to turn it into a green ally of the workers. Its design rationale is twofold: Firstly, to make the coffee-maker able to learn its own usage pattern. Secondly, to communicate persuasively and in real-time to users whether it is more efficient to leave the appliance on or off during certain periods of time along the workday. The goal is to explore a human-machine team towards energy efficiency and awareness, i.e. whether giving the initiative to users to decide how to operate the common appliances, but being assisted by them, is a better choice than automation or mere informative eco-feedback.")
    EcoAwareCoffeeMaker.save()
    print(EcoAwareCoffeeMaker)

    #EnergyPuppet=InteractiveSystem.objects.get(name="Energy Puppet");
    EnergyPuppet=InteractiveSystem(name="Energy Puppet", reference="Abdelmohsen, S., & Do, E. Y. L. (2008). Energy puppet: An ambient awareness interface for home energy consumption.", abstract="The Energy Puppet is an ambient display device that provides peripheral awareness of energy consumption for individual home appliances. The display produces different 'pet-like' behavioral reactions according to energy use patterns of the appliances to give homeowners an indication of their energy consumption status. The puppet would raise its 'arms' in victory to display normal consumption rate, or its 'eyes' would change color to red and 'roar' to warn the homeowners when the specific appliance reaches dangerously high consumption rates. The assumption is that the awareness of energy consumption could affect how people consume and control energy use in their households. This paper describes the usage scenarios and the design and implementation of Energy Puppet and discusses future research directions.")
    EnergyPuppet.save()
    print(EnergyPuppet)

    #USEM=InteractiveSystem.objects.get(name="USEM");
    USEM=InteractiveSystem(name="USEM", reference="Masoodian, M., André, E., Kugler, M., Reinhart, F., Rogers, B., & Schlieper, K. (2014). USEM: A ubiquitous smart energy management system for residential homes.", abstract="With the ever-increasing worldwide demand for energy, and the limited available energy resources, there is a growing need to reduce our energy consumption whenever possible. Therefore, over the past few decades a range of technologies have been proposed to assist consumers with reducing their energy use. Most of these have focused on decreasing energy consumption in the industry, transport, and services sectors. In more recent years, however, growing attention has been given to energy use in the residential sector, which accounts for nearly 30 percent of total energy consumption in the developed countries. Here we present one such system, which aims to assist residential users with monitoring their energy usage and provides mechanisms for setting up and controlling their home appliances to conserve energy. We also describe a user study we have conducted to evaluate the effectiveness of this system in supporting its users with a range of tools and visualizations developed for ubiquitous devices such as mobile phones and tablets. The findings of this study have shown the potential benefits of our system, and have identified areas of improvement that need to be addressed in the future.")
    USEM.save()
    print(USEM)

    #AmbientBatteryLevel=InteractiveSystem.objects.get(name="Ambient Battery Level");
    AmbientBatteryLevel=InteractiveSystem(name="Ambient Battery Level", reference="Elbanhawy, E. Y., Smith, A. F., & Moore, J. (2016, September). Towards an ambient awareness interface for home battery storage system. In Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing: Adjunct (pp. 1608-1613). ACM.", abstract="Roof-mounted photovoltaic (PV) generation is becoming more prevalent within the domestic setting. Recently battery systems have enabled households to store excess self-generated electricity for subsequent use. However the associated user-interfaces and displays can be hard to understand, potentially preventing households from optimizing their solar usage. This paper introduces a known method being deployed in a new context. It reports on on-going research that investigates the effect of in-home ambient light displays linked to the home battery system. The paper covers the design stage and potential feedback solutions to raise awareness and influence consumer behaviour to promote energy conservation. An Ambient Light System is proposed to enable better user feedback. The study outlines the design recommendation for an ambient light display to be used in an energy consumption context. Using such a display, households can optimize use of low Carbon solar energy within the home, thus minimizing grid electricity usage.")
    AmbientBatteryLevel.save()
    print(AmbientBatteryLevel)

    #eAMBI=InteractiveSystem.objects.get(name="eAMBI");
    eAMBI=InteractiveSystem(name="eAMBI", reference="Guna, J., & Pogacnik, M. (2013). Ambient visualization of energy consumption information. International SERIES on Information Systems and Management in Creative eMedia, (2), 37-42.", abstract="We present the eAMBI, an unobtrusive ambient visual interface for displaying the current electrical energy consumption information in real time. The system consists of a smart IP enabled electrical energy meter, a RaspberryPi embedded computer, a controllable colour led strip display and software components. Energy consumption data is stored on a service provider's smartgrid data server. This information is conveyed to the users by using various colour patterns in a subtle, yet informative way. A dynamic VU-meter like ambient lighting visualization was selected. The system is installed in a typical home environment and allows the users to perceive their energy consumption in real-time in an unobtrusive way and thus help them change their behaviour and possibly habits.")
    eAMBI.save()
    print(eAMBI)

    #EnergySavings=InteractiveSystem.objects.get(name="EnergySavings");
    EnergySavings=InteractiveSystem(name="EnergySavings", reference="Tran, Q. (2014, May). Promoting energy efficient behavior through energy-related feedback. In Collaboration Technologies and Systems (CTS), 2014 International Conference on (pp. 611-615). IEEE.", abstract="The ongoing process of urgent issues such as global warming, climate change and a lack of renewable resources induced by energy consumption has promoted energy efficiency. Establishing daily energy-saving behaviors in domestic households plays a crucial role in achieving energy efficiency. As a result, a number of human-computer interaction works have laid the research on providing home residences with an awareness of energy conservation through energy-related feedback. Most of the researches focused on how to make feedback persuasive in conserving energy to home inhabitants. This paper aims at addressing neglected topics found in the literature review concerning how to bring energy feedback to novices at energy conservation and maintain their motivation for sustainable energy behavior in the long run. We also developed a mobile prototype to clarify our proposal.")
    EnergySavings.save()
    print(EnergySavings)

    #PersonalEnergyDashboard=InteractiveSystem.objects.get(name="Personal Energy Dashboard");
    PersonalEnergyDashboard=InteractiveSystem(name="Personal Energy Dashboard", reference="Colley, J. A., Bedwell, B., Crabtree, A., & Rodden, T. (2013, September). Exploring Reactions to Widespread Energy Monitoring. In IFIP Conference on Human-Computer Interaction (pp. 91-108). Springer Berlin Heidelberg.", abstract="This paper explores the measurement, apportionment and representation of widespread energy monitoring. We explicate the accountability to users of the data collected by this type of monitoring when it is presented to them as a single daylong picture. We developed a technology probe that combines energy measurement from the home, workplace and the journeys that connect these spaces. Through deployment of this probe with five users for one month we find that measurement need not be seamless for it to be accountable; that apportionment is key to making consumption for communal spaces accountable and that people can readily make useful inferences about their energy consumption from daylong pictures formed from widespread monitoring. Finally, we present four issues raised by the probe – the nature of real world monitoring, the dynamic and social nature of apportionment, disclosure of energy data and alignment of incentives with consumption – that need to be addressed in future research.")
    PersonalEnergyDashboard.save()
    print(PersonalEnergyDashboard)

    #HousingCooperativeEnergyApp=InteractiveSystem.objects.get(name="Housing Cooperative Energy App");
    HousingCooperativeEnergyApp=InteractiveSystem(name="Housing Cooperative Energy App", reference="Hasselqvist, H., Bogdan, C., & Kis, F. (2016, June). Linking Data to Action: Designing for Amateur Energy Management. In Proceedings of the 2016 ACM Conference on Designing Interactive Systems (pp. 473-483). ACM.", abstract="Design of eco-feedback has primarily aimed at persuading individuals to change behaviours into more environmentally sustainable ones. However, it has been questioned how effective such feedback is in supporting long-term change. As an alternative focus for energy feedback, we present a case study of amateur energy management work in apartment buildings owned by housing cooperatives, and the design of an app that aims to stimulate and support cooperatives in taking energy actions that significantly reduce the cooperative's collective energy use. By linking energy data to energy actions, the users can see how actions taken in their own and other cooperatives affected the energy use, learn from each other's experiences and become motivated as energy amateurs. Based on our housing cooperative case, we reflect on design aspects to consider when designing for energy management in amateur settings.")
    HousingCooperativeEnergyApp.save()
    print(HousingCooperativeEnergyApp)

    #WhatAWatt=InteractiveSystem.objects.get(name="What-a-Watt");
    WhatAWatt=InteractiveSystem(name="What-a-Watt", reference="Quintal, F., Pereira, L., Nunes, N. J., & Nisi, V. (2015, April). What-a-Watt: exploring electricity production literacy through a long term eco-feedback study. In Sustainable Internet and ICT for Sustainability (SustainIT), 2015 (pp. 1-6). IEEE.", abstract="This paper presents the design, implementation and evaluation of an eco-feedback system capable of providing detailed household consumption information and also real-time production breakdown per energy source. We build on recent studies reporting an increased awareness generated by ecofeedback systems that also integrate micro-production information, taking advantage of a closed grid production network on an island with a high concentration of renewables, we deployed the What-a-Watt system in a building with 9 households for a period of 34 consecutive weeks. Results show that all the participating families have shown increased awareness of the production and distribution of electricity, thus becoming more familiarized with concepts such as the different sources of energy and how their availability relates to external variables such as weather conditions and time of day. Furthermore, our results also show, that the families using our system have managed to reduce their overall consumption. This research is a first attempt to provide more effective eco-feedback systems to consumers by integrating complex Smartgrid information in the feedback.")
    WhatAWatt.save()
    print(WhatAWatt)


    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Year2005 = Characteristic(name="2005", description="")
    Year2005.save()
    Year2005.interactive_systems.add(
        PowerAwareCord,
        );
    Year2005.save()

    Year2007 = Characteristic(name="2007", description="")
    Year2007.save()
    Year2007.interactive_systems.add(
        OaksAndCounting,
        FlowerLamp,
        );
    Year2007.save()

    Year2008 = Characteristic(name="2008", description="")
    Year2008.save()
    Year2008.interactive_systems.add(
        EnergyPuppet,
        );
    Year2008.save()

    Year2009 = Characteristic(name="2009", description="")
    Year2009.save()
    Year2009.interactive_systems.add(
        Boel,
        HandyFeedback,
        MobileEcd,
        NuageVert,
        PullMeOutPowerCord,
        StationaryEcd,
        Tenere,
        WattBot,
        );
    Year2009.save()

    Year2010 = Characteristic(name="2010", description="")
    Year2010.save()
    Year2010.interactive_systems.add(
        Coralog,
        ePoint,
        EnergyAwareClock,
        EnergyLocalLamp,
        EnergyOrb,
        LightningFeedbackDisplay,
        WattLite,
        Wattson,
        );
    Year2010.save()

    Year2011 = Characteristic(name="2011", description="")
    Year2011.save()
    Year2011.interactive_systems.add(
        AbstractAmbient,
        EnergyPlant,
        EnergyWiz,
        ForeWatch,
        Flo,
        PowerSocket,
        ShareAwareLight,
        Velix,
        );
    Year2011.save()

    Year2012 = Characteristic(name="2012", description="")
    Year2012.save()
    Year2012.interactive_systems.add(
        EnergyLife,
        FigureEnergy,
        LocalEnergyIndicator,
        PersonalizedEcoFeedback,
        PowerAdvisor,
        StationEnr,
        WattsWatt,

        );
    Year2012.save()

    Year2013 = Characteristic(name="2013", description="")
    Year2013.save()
    Year2013.interactive_systems.add(
        AgentSwitch,
        CustomisableDashboard,
        EnergyDub,
        Hems,
        LimitEcoFeedback,
        POEM,
        PersonalEnergyDashboard,
        RevealIt,
        WATTSBurning,
        eAMBI,
        );
    Year2013.save()

    Year2014 = Characteristic(name="2014", description="")
    Year2014.save()
    Year2014.interactive_systems.add(
        AgentB,
        BizWatts,
        ConversationWashMachine,
        EcoAwareCoffeeMaker,
        EnergySavings,
        PowerViz,
        USEM,
        );
    Year2014.save()

    Year2015 = Characteristic(name="2015", description="")
    Year2015.save()
    Year2015.interactive_systems.add(
        Ecosphere,
        IDO,
        TireeEnergyPulse,
        WhatAWatt,
        eForecast,
        );
    Year2015.save()

    Year2016 = Characteristic(name="2016", description="")
    Year2016.save()
    Year2016.interactive_systems.add(
        AmbientBatteryLevel,
        ArchiExpression,
        EnergyTree,
        HeatDial,
        HousingCooperativeEnergyApp,
        MyLocalEnergy,
        TariffAgent,
        TemperatureCalendar,
        WattISee,

        );
    Year2016.save()

    Year2017 = Characteristic(name="2017", description="")
    Year2017.save()
    Year2017.interactive_systems.add(
        EcoFeedback,
        );
    Year2017.save()

    Year = Criterium(name="Year")
    Year.save()
    Year.characteristics.add(Year2005, Year2007, Year2008, Year2009, Year2010, Year2011, Year2012, Year2013, Year2014, Year2015, Year2016, Year2017)
    Year.save()

    Meta = Entity(name="Meta")
    Meta.save()
    Meta.criteria.add(Year)
    Meta.save()

    Reducing = Characteristic(name="reducing or sharing energy demand", description="")
    Reducing.save()
    Reducing.interactive_systems.add(
        FigureEnergy,
        NuageVert,
        FlowerLamp,
        EnergyPlant,
        EnergyTree,
        EnergyAwareClock,
        RevealIt,
        HandyFeedback,
        PowerAdvisor,
        PersonalizedEcoFeedback,
        LimitEcoFeedback,
        EnergyLife,
        AbstractAmbient,
        PowerViz,
        EnergyDub,
        Hems,
        EnergyOrb,
        WattsWatt,
        EnergyWiz,
        WattLite,
        AgentB,
        PowerAwareCord,
        ShareAwareLight,
        Wattson,
        Tenere,
        ePoint,
        PowerSocket,
        PullMeOutPowerCord,
        Coralog,
        WattBot,
        Flo,
        StationaryEcd,
        MobileEcd,
        LightningFeedbackDisplay,
        OaksAndCounting,
        Boel,
        HeatDial,
        AgentSwitch,
        TemperatureCalendar,
        Velix,
        EcoFeedback,
        WATTSBurning,
        IDO,
        MyLocalEnergy,
        POEM,
        eForecast,
        Ecosphere,
        ArchiExpression,
        BizWatts,
        EcoAwareCoffeeMaker,
        EnergyPuppet,
        USEM,
        eAMBI,
        EnergySavings,
        PersonalEnergyDashboard,
        HousingCooperativeEnergyApp
    )
    Reducing.save()

    ShiftingLoadPeak = Characteristic(name="shifting energy demand to off-peak load hours", description="shfting energy demand to off-peak hours of global energy consumption.")
    ShiftingLoadPeak.save()
    ShiftingLoadPeak.interactive_systems.add(
        HeatDial,
        AgentSwitch,
        eForecast,
    )
    ShiftingLoadPeak.save()
    StoringLoadPeak = Characteristic(name="storing energy during off-peak load hours", description="storing energy during off-peak hours of global energy consumption to consume or share it later.")
    StoringLoadPeak.save()
    StoringLoadPeak.interactive_systems.add(
        AgentB
        )
    StoringLoadPeak.save()

    ShiftingGreenPeak = Characteristic(name="shfting energy demand to peak green hours", description="shifting energy consumption to peak hours of local green energy production.")
    ShiftingGreenPeak.save()
    ShiftingGreenPeak.interactive_systems.add(
        ForeWatch,
        EnergyLocalLamp,
        CustomisableDashboard,
        TireeEnergyPulse,
        ConversationWashMachine,
        StationEnr,
        TariffAgent,
        HeatDial,
        WattISee,
        eForecast,
        WhatAWatt

    )
    ShiftingGreenPeak.save()

    StoringGreenPeak = Characteristic(name="storing energy during peak green hours", description="storing energy during peak hours of local green energy production to consume or share it later.")
    StoringGreenPeak.save()
    StoringGreenPeak.interactive_systems.add(
        AmbientBatteryLevel,
        LocalEnergyIndicator,
        )
    StoringGreenPeak.save()

    EnergySobriety = Criterium(name="energy sobriety")
    EnergySobriety.save()
    EnergySobriety.characteristics.add(Reducing,ShiftingLoadPeak, StoringLoadPeak)
    EnergySobriety.save()

    EnergyCleanliness = Criterium(name="energy cleanliness")
    EnergyCleanliness.save()
    EnergyCleanliness.characteristics.add(ShiftingGreenPeak, StoringGreenPeak)
    EnergyCleanliness.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    AnySpace =Characteristic(name="any space", description="target any social space, e.g., a power cord designed for any space with a power outlet")
    AnySpace.save()
    AnySpace.interactive_systems.add(PowerAwareCord, ShareAwareLight, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, EcoAwareCoffeeMaker, PersonalEnergyDashboard)
    AnySpace.save()

    DomesticSpace =Characteristic(name="domestic space", description="target domestic spaces, e.g., a connected object designed for domestic space only")
    DomesticSpace.save()
    DomesticSpace.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, Hems, EnergyOrb, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, LocalEnergyIndicator, AgentB, Wattson, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, Boel, TariffAgent, HeatDial, AgentSwitch, Velix, EcoFeedback, WATTSBurning, MyLocalEnergy, eForecast, Ecosphere, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, HousingCooperativeEnergyApp, WhatAWatt)
    DomesticSpace.save()

    CollectiveSpace =Characteristic(name="collective space", description="target collective spaces, e.g., a connected kiosk designed for the workspace only")
    CollectiveSpace.save()
    CollectiveSpace.interactive_systems.add(WattLite, StationEnr, OaksAndCounting, IDO, POEM, BizWatts)
    CollectiveSpace.save()

    PublicSpace =Characteristic(name="public space", description="target public spaces, e.g., a connected and projected cloud on a column of smoke designed for public places only")
    PublicSpace.save()
    PublicSpace.interactive_systems.add(TemperatureCalendar, WattISee, ArchiExpression)
    PublicSpace.save()

    Target = Criterium(name="target")
    Target.save()
    Target.characteristics.add(AnySpace,DomesticSpace, CollectiveSpace, PublicSpace)
    Target.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Manual =Characteristic(name="manual", description="allow manual control of appliances, e.g., the user turn off or on the lamp of the bedroom")
    Manual.save()
    Manual.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, Hems, EnergyOrb, WattsWatt, EnergyWiz, WattLite, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, LocalEnergyIndicator, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, StationEnr, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, TariffAgent, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, ArchiExpression, BizWatts, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    Manual.save()

    SemiAutomatic =Characteristic(name="semi-automatic", description="allow remote control of appliances, e.g., the user can turn off or on the lamp of the bedroom remotely")
    SemiAutomatic.save()
    SemiAutomatic.interactive_systems.add(ConversationWashMachine, AgentB, TariffAgent, HeatDial, IDO, MyLocalEnergy, USEM)
    SemiAutomatic.save()

    Automatic =Characteristic(name="automatic", description="allow automatic control of appliances, e.g., when the user enters the bedroom, the system turns on the lamp")
    Automatic.save()
    Automatic.interactive_systems.add(TariffAgent, IDO, MyLocalEnergy)
    Automatic.save()

    Control = Criterium(name="control")
    Control.save()
    Control.characteristics.add(Manual, SemiAutomatic, Automatic)
    Control.save()

    Context = Entity(name="Context")
    Context.save()
    Context.criteria.add(EnergySobriety,EnergyCleanliness, Target, Control)
    Context.save()


    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()


    DataEnergyConsumption =Characteristic(name="energy consumption", description="use data on energy consumption e.g., grey power consumed by the household")
    DataEnergyConsumption.save()
    DataEnergyConsumption.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, Hems, EnergyOrb, WattsWatt, EnergyWiz, WattLite, CustomisableDashboard, ConversationWashMachine, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, StationEnr, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, TariffAgent, HeatDial, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, Ecosphere, ArchiExpression, BizWatts, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    DataEnergyConsumption.save()

    DataEnergyProduction=Characteristic(name="energy production", description="use data on production consumption e.g., yesterday solar energy production of France")
    DataEnergyProduction.save()
    DataEnergyProduction.interactive_systems.add(AmbientBatteryLevel, WhatAWatt, WattISee, TariffAgent, StationEnr, LocalEnergyIndicator, EnergyLocalLamp, ConversationWashMachine, CustomisableDashboard, TireeEnergyPulse, ForeWatch)
    DataEnergyProduction.save()

    DataEnergyStorage=Characteristic(name="energy storage", description="use data on storage consumption e.g., green energy stored by the workplace since the last month")
    DataEnergyStorage.save()
    DataEnergyStorage.interactive_systems.add(AgentB, LocalEnergyIndicator, StationEnr, Flo, AmbientBatteryLevel)
    DataEnergyStorage.save()

    DataEnergyDistribution=Characteristic(name="energy distribution", description="use historical data on energy e.g., green energy distributed in London")
    DataEnergyDistribution.save()
    DataEnergyDistribution.interactive_systems.add(ShareAwareLight, Tenere, PullMeOutPowerCord, Flo, AmbientBatteryLevel)
    DataEnergyDistribution.save()

    DataEnergySaving=Characteristic(name="energy saving", description="use historical data on energy e.g., last month energy savings in the living room")
    DataEnergySaving.save()
    DataEnergySaving.interactive_systems.add(PersonalizedEcoFeedback, LimitEcoFeedback, FigureEnergy, NuageVert, AgentB, EnergyTree, AgentSwitch, TemperatureCalendar, Velix, MyLocalEnergy, BizWatts, EcoAwareCoffeeMaker, EnergySavings)
    DataEnergySaving.save()

    DataType = Criterium(name="type")
    DataType.save()
    DataType.characteristics.add(DataEnergyConsumption,DataEnergyProduction, DataEnergyStorage, DataEnergyDistribution, DataEnergySaving)
    DataType.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()


    DataHistorical=Characteristic(name="historical", description="use historical data on energy e.g., household wind energy consumption of the last month")
    DataHistorical.save()
    DataHistorical.interactive_systems.add(HandyFeedback, PowerAdvisor, ForeWatch, EnergyLife, TireeEnergyPulse, EnergyWiz, PersonalizedEcoFeedback, PowerViz, LimitEcoFeedback, CustomisableDashboard, Hems, ConversationWashMachine, FigureEnergy, WattsWatt, EnergyDub, RevealIt, EnergyPlant, WattLite, EnergyAwareClock, StationEnr, Coralog, WattBot, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, Ecosphere, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp,WhatAWatt)
    DataHistorical.save()

    DataImmediate=Characteristic(name="immediate", description="use immediate data on energy e.g., actual gray energy distribution of country")
    DataImmediate.save()
    DataImmediate.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, HandyFeedback, PowerAdvisor, ForeWatch, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, Hems, EnergyOrb, EnergyWiz, WattLite, TireeEnergyPulse, LocalEnergyIndicator, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, TariffAgent, HeatDial, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, ArchiExpression, BizWatts, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    DataImmediate.save()

    DataForecast=Characteristic(name="forecast", description="use forecast data on energy e.g., household bioenergy production for the next 2 days")
    DataForecast.save()
    DataForecast.interactive_systems.add(ForeWatch, TireeEnergyPulse, Hems, ConversationWashMachine, FigureEnergy, EnergyDub, AgentB, TariffAgent, AgentSwitch, eForecast, USEM)
    DataForecast.save()

    DataTemporalScale = Criterium(name="temporal scale")
    DataTemporalScale.save()
    DataTemporalScale.characteristics.add(DataHistorical,DataImmediate, DataForecast)
    DataTemporalScale.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    DataAppliance=Characteristic(name="appliance", description="use energy data related to appliances e.g., last month energy production of a solar panel")
    DataAppliance.save()
    DataAppliance.interactive_systems.add(HandyFeedback, EnergyLife, PowerViz, Hems, ConversationWashMachine, FigureEnergy, AgentB, EnergyLocalLamp, PowerAwareCord, ShareAwareLight, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot,LightningFeedbackDisplay, HeatDial, IDO, MyLocalEnergy, POEM, BizWatts, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, EnergySavings)
    DataAppliance.save()


    DataRoom=Characteristic(name="room" , description="use energy data related to rooms e.g., power consumption of the bathroom")
    DataRoom.save()
    DataRoom.interactive_systems.add(PowerViz, Hems, TemperatureCalendar, IDO, MyLocalEnergy, POEM, USEM)
    DataRoom.save()

    DataBuilding=Characteristic(name="building" , description="use energy data related to buildings e.g., forecast energy storage of the workplace for the next month")
    DataBuilding.save()
    DataBuilding.interactive_systems.add(FigureEnergy, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, Hems, EnergyOrb, WattsWatt, EnergyWiz, WattLite, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, LocalEnergyIndicator, AgentB, Wattson, StationEnr, WattBot, Flo, StationaryEcd, MobileEcd, OaksAndCounting, Boel, TariffAgent, AgentSwitch, Velix, EcoFeedback, WATTSBurning, MyLocalEnergy, POEM, eForecast, Ecosphere, ArchiExpression, USEM, eAMBI, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    DataBuilding.save()

    DataNeighborhood=Characteristic(name="neighborhood", description="use energy data related to neighborhoods e.g., green power consumption of a district")
    DataNeighborhood.save()
    DataNeighborhood.interactive_systems.add(EnergyWiz, Boel)
    DataNeighborhood.save()

    DataCity=Characteristic(name="city", description="use energy data related to cities e.g., actual nuclear energy distributed in Paris")
    DataCity.save()
    DataCity.interactive_systems.add(NuageVert, RevealIt)
    DataCity.save()

    DataCountry=Characteristic(name="country",  description="use energy data related to a countries e.g., last year hydraulic energy consumption of France")
    DataCountry.save()
    DataCountry.interactive_systems.add(WattISee)
    DataCountry.save()

    DataSpatialScale = Criterium(name="spatial scale")
    DataSpatialScale.save()
    DataSpatialScale.characteristics.add(DataAppliance, DataRoom, DataBuilding, DataNeighborhood, DataCity, DataCountry)
    DataSpatialScale.save()

    Data = Entity(name="Data", description="functions implemented to assit users")
    Data.save()
    Data.criteria.add(DataType, DataTemporalScale, DataSpatialScale)
    Data.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Activating=Characteristic(name="activating energy", description="consume energy")
    Activating.save()
    Activating.interactive_systems.add(FigureEnergy, FlowerLamp, EnergyPlant, EnergyAwareClock, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, Hems, EnergyOrb, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, LocalEnergyIndicator, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, TariffAgent, HeatDial, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, ArchiExpression, BizWatts, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    Activating.save()

    Collecting=Characteristic(name="collecting energy", description="produce energy")
    Collecting.save()
    Collecting.interactive_systems.add(ArchiExpression)
    Collecting.save()

    Keeping=Characteristic(name="keeping energy", description="store energy")
    Keeping.save()
    Keeping.interactive_systems.add(FigureEnergy, EnergyAwareClock, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyDub, Hems, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, AgentB, WattBot, Flo, MobileEcd, TariffAgent, AgentSwitch, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, ArchiExpression, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    Keeping.save()

    Sharing=Characteristic(name="sharing energy" , description="distribute energy")
    Sharing.save()
    Sharing.interactive_systems.add(PowerAwareCord, ShareAwareLight, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Flo, WattISee)
    Sharing.save()

    Materialization = Criterium(name="materialization")
    Materialization.save()
    Materialization.characteristics.add(Activating, Collecting, Keeping, Sharing)
    Materialization.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Forecast=Characteristic(name="forecast", description="project the actual behavior in the future to predict future behavior consequences")
    Forecast.save()
    Forecast.interactive_systems.add(ForeWatch, TireeEnergyPulse, PersonalizedEcoFeedback, LimitEcoFeedback, CustomisableDashboard, Hems, ConversationWashMachine, FigureEnergy, AgentB, StationEnr, TariffAgent, AgentSwitch, MyLocalEnergy, eForecast, USEM)
    Forecast.save()

    Suggestion=Characteristic(name="suggestion", description="recommend actions to get more desirable behavior consequences")
    Suggestion.save()
    Suggestion.interactive_systems.add(HousingCooperativeEnergyApp, USEM, EcoAwareCoffeeMaker, MyLocalEnergy, IDO, WATTSBurning, EcoFeedback, Velix, AgentSwitch, TariffAgent, ConversationWashMachine, LimitEcoFeedback, TireeEnergyPulse, EnergyLife)
    Suggestion.save()

    Evaluation=Characteristic(name="evaluation", description="position behavior consequences on a scale from undesirable to desirable")
    Evaluation.save()
    Evaluation.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, EnergyDub, EnergyOrb, WattsWatt, EnergyWiz, WattLite, ConversationWashMachine, LocalEnergyIndicator, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, StationEnr, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, HeatDial, TemperatureCalendar, Velix, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, ArchiExpression, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, HousingCooperativeEnergyApp)
    Evaluation.save()


    Simulation=Characteristic(name="simulation", description="simulate behavior changes at different moments and locations to observe its consequences")
    Simulation.save()
    Simulation.interactive_systems.add(FigureEnergy, AgentB, StationEnr, HeatDial, AgentSwitch, WattISee)
    Simulation.save()


    ImmediateFeedback=Characteristic(name="immediate feedback", description="return immediate information on behavior consequences")
    ImmediateFeedback.save()
    ImmediateFeedback.interactive_systems.add(FigureEnergy, NuageVert, FlowerLamp, EnergyPlant, EnergyAwareClock, HandyFeedback, ForeWatch, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyLocalLamp, Hems, EnergyOrb, EnergyWiz, WattLite, LocalEnergyIndicator, AgentB, PowerAwareCord, ShareAwareLight, Wattson, Tenere, StationEnr, ePoint, PowerSocket, WattBot, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, Boel, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, ArchiExpression, EcoAwareCoffeeMaker, EnergyPuppet, USEM, AmbientBatteryLevel, eAMBI, EnergySavings, WhatAWatt)
    ImmediateFeedback.save()


    CumulativeFeedback=Characteristic(name="cumulative feedback", description="return information on accumulated behavior consequences within a defined period")
    CumulativeFeedback.save()
    CumulativeFeedback.interactive_systems.add(PowerAdvisor, EnergyWiz, PersonalizedEcoFeedback, AbstractAmbient, LimitEcoFeedback, CustomisableDashboard, Hems, FigureEnergy, AgentB, EnergyDub, EnergyPlant, EnergyAwareClock, EnergyTree, Tenere, StationEnr, PullMeOutPowerCord, Coralog, WattBot, OaksAndCounting, TariffAgent, HeatDial, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    CumulativeFeedback.save()


    TemporalComparison=Characteristic(name="temporal comparison", description="compare behavior consequences at different moments")
    TemporalComparison.save()
    TemporalComparison.interactive_systems.add(HandyFeedback, PowerAdvisor, ForeWatch, EnergyLife, TireeEnergyPulse, EnergyWiz, PowerViz, LimitEcoFeedback, CustomisableDashboard, Hems, ConversationWashMachine, FigureEnergy, AgentB, WattsWatt, EnergyDub, RevealIt, EnergyPlant, WattLite, EnergyAwareClock, StationEnr, Coralog, TariffAgent, TemperatureCalendar, Velix, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, Ecosphere, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    TemporalComparison.save()

    SpatialComparison=Characteristic(name="spatial comparison", description="compare behavior consequences at different locations")
    SpatialComparison.save()
    SpatialComparison.interactive_systems.add(HandyFeedback, EnergyLife, PowerViz, Hems, ShareAwareLight, Tenere, WattBot, TemperatureCalendar, IDO, MyLocalEnergy, POEM, ArchiExpression, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard)
    SpatialComparison.save()

    SocialComparison =Characteristic(name="social comparison", description="compare behavior consequences with one or more social norms")
    SocialComparison.save()
    SocialComparison.interactive_systems.add(PowerAdvisor, EnergyWiz, WattsWatt, EnergyDub, RevealIt, EnergyTree, Flo, Boel, Velix, IDO, BizWatts, EnergySavings, HousingCooperativeEnergyApp)
    SocialComparison.save()

    Persuasion = Criterium(name="persuasion")
    Persuasion.save()
    Persuasion.characteristics.add(Forecast, Suggestion, Evaluation, Simulation, ImmediateFeedback, CumulativeFeedback, TemporalComparison, SpatialComparison, SocialComparison)
    Persuasion.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Challenge =Characteristic(name="challenge", description="set goals to an individual or to a group within a defined period")
    Challenge.save()
    Challenge.interactive_systems.add(PowerAdvisor, EnergyLife, EnergyWiz, EnergyDub, OaksAndCounting, Velix, BizWatts)
    Challenge.save()

    Competition =Characteristic(name="competition", description="put individuals or groups in competition to reach the same goal; e.g., leaderboards")
    Competition.save()
    Competition.interactive_systems.add(PowerAdvisor,EnergyWiz,WattsWatt,EnergyDub,RevealIt,EnergyTree,Flo, Boel, BizWatts, EnergySavings)
    Competition.save()

    Collaboration =Characteristic(name="collaboration", description="allow individuals cooperating to reach the same goal")
    Collaboration.save()
    Collaboration.interactive_systems.add(EnergyTree, PowerAwareCord, ShareAwareLight, Tenere, StationEnr, PullMeOutPowerCord, Flo, WattISee, BizWatts)
    Collaboration.save()

    Progression =Characteristic(name="progression", description="follow progression of individuals or groups towards the goal")
    Progression.save()
    Progression.interactive_systems.add(PowerAdvisor,EnergyWiz,EnergyTree,)
    Progression.save()

    SocialInteraction =Characteristic(name="social interaction", description="allows social exchanges among individuals or groups; e.g., social network")
    SocialInteraction.save()
    SocialInteraction.interactive_systems.add(EnergyLife,EnergyWiz,EnergyDub, WattLite, Tenere, Velix, WattISee, ArchiExpression, BizWatts, EcoAwareCoffeeMaker, EnergySavings, HousingCooperativeEnergyApp)
    SocialInteraction.save()

    Personalization =Characteristic(name="personalization", description="adapt to the values of individuals or groups")
    Personalization.save()
    Personalization.interactive_systems.add(PersonalizedEcoFeedback, CustomisableDashboard, EnergyPlant)
    Personalization.save()

    Achievement =Characteristic(name="achievement", description="promote publicly the desirable actions of individuals or groups; e.g., points or badges")
    Achievement.save()
    Achievement.interactive_systems.add(EnergyLife,WattsWatt,EnergyDub, Velix, BizWatts)
    Achievement.save()

    Reward=Characteristic(name="reward", description="promote immediately a desirable action of individuals or groups; e.g., virtual items")
    Reward.save()
    Reward.interactive_systems.add(FigureEnergy,WattsWatt, TariffAgent, Velix)
    Reward.save()

    Gamification = Criterium(name="gamification")
    Gamification.save()
    Gamification.characteristics.add(Challenge, Competition, Collaboration, Progression, SocialInteraction, Personalization, Achievement, Reward)
    Gamification.save()


    Function = Entity(name="Function")
    Function.save()
    Function.criteria.add(Materialization, Persuasion, Gamification)
    Function.save()


    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Graphical =Characteristic(name="graphical", description="employ pixel-based interfaces; e.g., smartphone, tablet, PC, projection, or web application")
    Graphical.save()
    Graphical.interactive_systems.add(FigureEnergy, RevealIt, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyDub, Hems, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, AgentB, Coralog, WattBot, LightningFeedbackDisplay, OaksAndCounting, TariffAgent, HeatDial, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, Ecosphere, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt,  StationEnr, NuageVert)
    Graphical.save()

    Physical =Characteristic(name="physical", description="employ physical-based interfaces; e.g., restyled everyday object, connected object, or physical installation")
    Physical.save()
    Physical.interactive_systems.add(FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, EnergyLocalLamp, EnergyOrb, WattLite, TireeEnergyPulse, LocalEnergyIndicator, PowerAwareCord, ShareAwareLight, Wattson, Tenere, StationEnr, ePoint, PowerSocket, PullMeOutPowerCord, Flo, StationaryEcd, MobileEcd, Boel, WattISee, ArchiExpression, EcoAwareCoffeeMaker, EnergyPuppet, AmbientBatteryLevel, eAMBI)
    Physical.save()

    Ambient =Characteristic(name="ambient", description="employ ambient interfaces e.g., a web application or a connected object changing color from red to green progressively")
    Ambient.save()
    Ambient.interactive_systems.add(ForeWatch, AbstractAmbient, PowerViz, RevealIt, FlowerLamp, EnergyPlant, EnergyTree, EnergyAwareClock, EnergyLocalLamp, EnergyOrb, WattLite, TireeEnergyPulse, LocalEnergyIndicator, PowerAwareCord, ShareAwareLight, Wattson, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Coralog, Flo, StationaryEcd, MobileEcd, LightningFeedbackDisplay, OaksAndCounting, Boel, TemperatureCalendar, WattISee, ArchiExpression, EcoAwareCoffeeMaker, EnergyPuppet, AmbientBatteryLevel, eAMBI)
    Ambient.save()

    Type=Criterium(name="type")
    Type.save()
    Type.characteristics.add(Graphical, Physical, Ambient)
    Type.save()

    Individual=Characteristic(name="individual", description="visible by a unique individual; e.g., a mobile app")
    Individual.save()
    Individual.interactive_systems.add(FigureEnergy, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, PowerViz, EnergyDub, Hems, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, AgentB, Coralog, WattBot, TariffAgent, HeatDial, AgentSwitch, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, Ecosphere, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    Individual.save()

    Room=Characteristic(name="room", description="visible by individuals in a room; e.g., a lamp in a the bathroom")
    Room.save()
    Room.interactive_systems.add(eAMBI, AmbientBatteryLevel, EnergyPuppet, EcoAwareCoffeeMaker, ArchiExpression, WattISee, WATTSBurning, TemperatureCalendar, Boel, OaksAndCounting, LightningFeedbackDisplay, MobileEcd, StationaryEcd, Flo, Coralog, PullMeOutPowerCord, PowerSocket, ePoint, StationEnr, Tenere, Wattson, ShareAwareLight, PowerAwareCord, FlowerLamp, EnergyLocalLamp, EnergyOrb, EnergyTree, EnergyAwareClock, WattLite, EnergyPlant, LocalEnergyIndicator, RevealIt, AbstractAmbient, PowerViz)
    Room.save()

    Building=Characteristic(name="building", description="visible by individuals in the street;  e.g., a projected pattern on a building")
    Building.save()
    Building.interactive_systems.add(Boel)
    Building.save()

    City=Characteristic(name="city", description="visible by individuals in the city; e.g., an object flying above a city")
    City.save()
    City.interactive_systems.add(NuageVert)
    City.save()

    Visibility=Criterium(name="visibility")
    Visibility.save()
    Visibility.characteristics.add(Individual, Room, Building, City)
    Visibility.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()

    Mobile=Characteristic(name="mobile", description="accessible by a unique individual; e.g., a mobile app")
    Mobile.save()
    Mobile.interactive_systems.add(FigureEnergy, HandyFeedback, PowerAdvisor, ForeWatch, PersonalizedEcoFeedback, LimitEcoFeedback, EnergyLife, AbstractAmbient, PowerViz, EnergyDub, Hems, WattsWatt, EnergyWiz, CustomisableDashboard, TireeEnergyPulse, ConversationWashMachine, AgentB, Coralog, WattBot, TariffAgent, HeatDial, AgentSwitch, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, POEM, eForecast, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt, Flo, MobileEcd)
    Mobile.save()

    FixedAnySpace=Characteristic(name="fixed on any space", description="accessible in specific spaces; e.g., a connected object plugged in the car")
    FixedAnySpace.save()
    FixedAnySpace.interactive_systems.add(PowerAwareCord, ShareAwareLight, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, EcoAwareCoffeeMaker)
    FixedAnySpace.save()

    FixedDomesticSpace=Characteristic(name="fixed on a domestic space", description="accessible in domestic spaces; e.g., an everyday object in the living the room")
    FixedDomesticSpace.save()
    FixedDomesticSpace.interactive_systems.add(eAMBI, AmbientBatteryLevel, EnergyPuppet, Ecosphere, Boel, LightningFeedbackDisplay, StationaryEcd, Wattson, FlowerLamp, EnergyLocalLamp, EnergyOrb, EnergyAwareClock, LocalEnergyIndicator, EnergyPlant, LocalEnergyIndicator)
    FixedDomesticSpace.save()

    FixedCollectiveSpace=Characteristic(name="fixed on a collective space" , description="accessible in collective spaces; e.g., a physical installation in the entrance hall of a school")
    FixedCollectiveSpace.save()
    FixedCollectiveSpace.interactive_systems.add(WattLite, EnergyTree, StationEnr, OaksAndCounting)
    FixedCollectiveSpace.save()

    FixedPublicSpace=Characteristic(name="fixed on a public space", description="accessible in public spaces; e.g., a web application projected on the wall of a public space")
    FixedPublicSpace.save()
    FixedPublicSpace.interactive_systems.add(RevealIt, NuageVert, Boel, TemperatureCalendar, WattISee, ArchiExpression)
    FixedPublicSpace.save()

    Accessibility=Criterium(name="accessibility")
    Accessibility.save()
    Accessibility.characteristics.add(Mobile, FixedAnySpace, FixedDomesticSpace, FixedCollectiveSpace, FixedPublicSpace)
    Accessibility.save()

    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()


    MobileDevice=Characteristic(name="mobile device", description="e.g., smartphone, tablet, notebook")
    MobileDevice.save()
    MobileDevice.interactive_systems.add(HandyFeedback, PowerAdvisor, ForeWatch, EnergyLife, TireeEnergyPulse, EnergyWiz, PersonalizedEcoFeedback, AbstractAmbient, PowerViz, LimitEcoFeedback, CustomisableDashboard, Coralog, WattBot, WATTSBurning, MyLocalEnergy, EnergySavings, HousingCooperativeEnergyApp, WhatAWatt)
    MobileDevice.save()

    Web=Characteristic(name="web", description="e.g., web application, website")
    Web.save()
    Web.interactive_systems.add(PersonalEnergyDashboard, USEM, BizWatts, eForecast, POEM, IDO, EcoFeedback, Velix, AgentSwitch, HeatDial, TariffAgent, RevealIt, EnergyDub, WattsWatt, AgentB, FigureEnergy, ConversationWashMachine, Hems)
    Web.save()

    ProjectionDevice=Characteristic(name="projection device", description="e.g., video projection")
    ProjectionDevice.save()
    ProjectionDevice.interactive_systems.add(RevealIt, NuageVert, LightningFeedbackDisplay)
    ProjectionDevice.save()

    ConnectedObject=Characteristic(name="connected object", description="N/A")
    ConnectedObject.save()
    ConnectedObject.interactive_systems.add(EnergyPuppet, Ecosphere, TemperatureCalendar, MobileEcd, StationaryEcd, Flo, Wattson, EnergyPlant, LocalEnergyIndicator)
    ConnectedObject.save()

    EverydayObject=Characteristic(name="everyday object", description="e.g., lamp, power cord, radiator, or clock")
    EverydayObject.save()
    EverydayObject.interactive_systems.add(EnergyAwareClock, EnergyOrb, EnergyLocalLamp, FlowerLamp, PowerAwareCord, ShareAwareLight, Tenere, ePoint, PowerSocket, PullMeOutPowerCord, Boel, EcoAwareCoffeeMaker, AmbientBatteryLevel, eAMBI)
    EverydayObject.save()

    PhysicalInstallation=Characteristic(name="physical installation", description="e.g., connected kiosk, wall display, or art installation")
    PhysicalInstallation.save()
    PhysicalInstallation.interactive_systems.add(ArchiExpression, WattISee, OaksAndCounting, StationEnr, EnergyTree, WattLite)
    PhysicalInstallation.save()

    Support=Criterium(name="support")
    Support.save()
    Support.characteristics.add(MobileDevice,Web,ProjectionDevice, ConnectedObject, EverydayObject, PhysicalInstallation)
    Support.save()

    Interface = Entity(name="Interface")
    Interface.save()
    Interface.criteria.add(Type, Visibility, Accessibility, Support)
    Interface.save()


    print("sleeping...")
    time.sleep(duration)
    db.connections.close_all()
    ##############USER

    PassiveIndividual=Characteristic(name="individual", description="allow an individual to receive information without manipulation")
    PassiveIndividual.save()
    PassiveIndividual.interactive_systems.add(MobileEcd)
    PassiveIndividual.save()

    PassiveFamily=Characteristic(name="family", description="allow a family to receive information without manipulation")
    PassiveFamily.save()
    PassiveFamily.interactive_systems.add(AbstractAmbient, PowerViz, LocalEnergyIndicator, EnergyPlant, EnergyAwareClock, EnergyOrb, EnergyLocalLamp, FlowerLamp, Wattson, Flo, StationaryEcd, LightningFeedbackDisplay, Boel,  WATTSBurning, EnergyPuppet, AmbientBatteryLevel, eAMBI)
    PassiveFamily.save()

    PassiveGroup=Characteristic(name="group", description="allow a group to receive information without manipulation")
    PassiveGroup.save()
    PassiveGroup.interactive_systems.add(EcoAwareCoffeeMaker, OaksAndCounting, Coralog, PullMeOutPowerCord, PowerSocket, ePoint, Tenere, ShareAwareLight, PowerAwareCord, EnergyTree)
    PassiveGroup.save()


    PassiveCommunity=Characteristic(name="community", description="allow a community to receive information without manipulation")
    PassiveCommunity.save()
    PassiveCommunity.interactive_systems.add()
    PassiveCommunity.save()

    PassiveSociety=Characteristic(name="society", description="allow a society to receive information without manipulation")
    PassiveSociety.save()
    PassiveSociety.interactive_systems.add(ArchiExpression, WattISee, TemperatureCalendar, Boel, NuageVert, WattLite, RevealIt)
    PassiveSociety.save()

    Passivity=Criterium(name="passivity")
    Passivity.save()
    Passivity.characteristics.add(PassiveIndividual, PassiveFamily, PassiveGroup, PassiveCommunity, PassiveSociety)
    Passivity.save()

    ProactiveIndividual=Characteristic(name="individual", description="allow an individual to manipulate information")
    ProactiveIndividual.save()
    ProactiveIndividual.interactive_systems.add(HandyFeedback, PowerAdvisor, ForeWatch, EnergyLife, TireeEnergyPulse, EnergyWiz, PersonalizedEcoFeedback, PowerViz, LimitEcoFeedback, CustomisableDashboard, Hems, ConversationWashMachine, FigureEnergy, AgentB, WattsWatt, EnergyDub, EnergyPlant, EnergyAwareClock, Wattson, Coralog, WattBot, OaksAndCounting, TariffAgent, HeatDial, AgentSwitch, TemperatureCalendar, Velix, EcoFeedback, WATTSBurning, IDO, MyLocalEnergy, WattISee, POEM, eForecast, Ecosphere, BizWatts, USEM, EnergySavings, PersonalEnergyDashboard, HousingCooperativeEnergyApp, WhatAWatt)
    ProactiveIndividual.save()

    ProactiveFamily=Characteristic(name="family", description="allow a family to manipulate information")
    ProactiveFamily.save()
    ProactiveFamily.interactive_systems.add(Flo)
    ProactiveFamily.save()

    ProactiveGroup=Characteristic(name="group", description="allow an group to manipulate information")
    ProactiveGroup.save()
    ProactiveGroup.interactive_systems.add(StationEnr, WattLite)
    ProactiveGroup.save()

    ProactiveCommunity=Characteristic(name="community", description="allow a community to manipulate information")
    ProactiveCommunity.save()
    ProactiveCommunity.interactive_systems.add(HousingCooperativeEnergyApp, EnergySavings, Velix, EnergyWiz, EnergyLife)
    ProactiveCommunity.save()

    ProactiveSociety=Characteristic(name="society", description="allow a society to manipulate information")
    ProactiveSociety.save()
    ProactiveSociety.interactive_systems.add(RevealIt)
    ProactiveSociety.save()

    Proactivity=Criterium(name="proactivity")
    Proactivity.save()
    Proactivity.characteristics.add(ProactiveIndividual, ProactiveFamily, ProactiveGroup, ProactiveCommunity, ProactiveSociety)
    Proactivity.save()

    User = Entity(name="User")
    User.save()
    User.criteria.add(Proactivity, Passivity)
    User.save()
