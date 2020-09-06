---
author: Luis Nicolás Luarte Rodríguez
title: Role of orexin and opioid dynorphin peptides in obesity behavioral dysregulation
geometry: "left=4cm,right=4cm,top=1cm,bottom=2cm"
linestretch: 1.5
---

# Food-seeking behavior and uncertainty

Uncertainty can be understood as a measure of the expectation of the reward prediction error in a given environment. This measure of the difference between expected reward and current reward is encoded by dopamine neurons [@ZHGB75KH#Bayer_Glimcher_2005]. Furthermore, this system can modify decision-making policies based on the reward-prediction error [@87WR6HV3#Pessiglione_Etal_2006]. Food-seeking behavior can be conceptualized as series of decision-making actions occurring in an environment with varying grades of uncertainty, where the reward prediction error evaluates each feeding bout, and over a history of bouts, uncertainty over environment rewards is obtained.

## Environment uncertainty and food intake

Under higher uncertainty levels of environment food disposition, animal food-seeking bouts are increased, resulting in hoarding-type behavior, arguably a mechanism to prevent possible starvation [@C6Z374UG#Anselme_Güntürkün_2019]. However, this behavior can also be explained by food scarcity or insufficient energetic supply by the environment. The latter case does not necessarily predict uncertainty as this can be high on average, but volatile from time to time. Nevertheless, when constant food position changes alter feeding environment, an increased intake is observed [@NL4XYLRH#Forkman_1993], so food access variability can trigger, by itself, an increased food-seeking behavior. Sign-tracking also increases when uncertainty about reward probabilities also increases [@S8CHV5KG#Anselme_Robinson_Berridge_2013]. That is, motivation is increased under the uncertainty of reward delivery. In addition to modifying intake, uncertainty levels can affect energy expenditure [@LLLWQCZE#Bednekoff_Houston_1994], even when overall food levels are equated in predictable and unpredictable setting [@3GQMEPEH#Cuthill_2000].

## Uncertainty representations at neural level

If uncertainty can modulate food-seeking behavior in order to increase intake and better sustain energetic reserves. It is expected to have at least, to functional instances (1) a uncertainty sensing unit and (2) a reward processing unit, which can relay information to homeostatic-related and decision-making loci, to integrate such information a determine the next action to take. In humans such functional instances seems to be separated, where nucleus accumbens, thalamus and medial orbitofrontal cortex are more activated in unpredictable reward scenarios, and predictable scenarios with right superior temporal gyrus [@G5PZHPCI#Tanaka_Etal_2006]. Task-related brain activity is reduced in more predictable environments, likely by lowering mean prediction error, however, anterior cingulate cortex (ACC), shows augmented activation when predictability drops [@9SRBHI4W#Davis_Choi_Benoit_2010]. When situated in a learning task, ventral striatum has been related to short-term reward prediction, whereas dorsal striatum was related with long-term reward prediction [@G5PZHPCI#Tanaka_Etal_2006]. Short-term reward prediction is closely related to uncertain environments as immediate rewards don't provide any information about subsequent rewards, which is the opposite case of certain (or regular) environments, where each rewards provide all information to predict the next reward. Direct tracking of environment volatility shows that this is well represented in ACC, moreover, this ACC activity is modulated by volatility when reward is observed after an action is made, so the observed effect might imply a modulation of value assigned to the outcome given environment uncertainty [@BHR2NAEI#Behrens_Etal_2007].

When representing uncertainty of a given environment, an agent must pair the value obtained with the action performed. For each action possible the agent updates the value of action-reward based on the reward prediction error. The objective of the agent is to minimize the reward-prediction error. Thus, the uncertainty of a given environment is represented by the time taken, for a given agent, to converge into action-rewards value that minimize reward-prediction error.



## Models explaining food intake in obesity

### Reinforcement learning models

Temporal-difference learning models, state how agents can estimate reward values in uncertain environments. At each time-step, the agent computes de value of a given state considering (1) the estimated value (randomly initiated at first) and (2) the temporal-difference error which state the distance between the estimate of state value and the actual reward obtained in such state.

\begin{equation}
	V(S_t) \leftarrow V(S_t) + \alpha(Temporal \, Difference \, Error)
\end{equation}

$V(S_t)$ denotes the estimated value at a given state, and $\alpha$ is used to model the agent learning rate, that is, the rate at which state value is updated, and thus able to affect agent behavior. Additional parameter $\rho$ has been proposed to model sensitivity to reward [@JGKMEKV6#Huys_Etal_2013; @GU4KJGAS#Kroemer_Small_2016], such that the temporal difference error accounts for the subjective value of obtained rewards.

\begin{equation}
	Temporal \, Difference \, Error = \rho \times Reward - V(S_t)
\end{equation}

Obese subjects had shown reduced dorsal striatum activity to food rewards, which has been interpreted as reduced pleasure for food. However, simulations under previously presented model show another option, that is, obese subject show heightened reward sensitivity but decreased learning rates, ending in a lowered state value estimation [@GU4KJGAS#Kroemer_Small_2016]. Modeled learning rates measures, had shown that this is the case in obese subjects, moreover, it pointed that negative prediction errors (equivalent of temporal difference error) were used to a lesser extent than lean subjects, whereas positive errors showed no differences [@DBGUDZRL#Mathar_Etal_2017]. This points to a difficulty to update reward or state values when the estimated reward is higher than the actual reward, possibly reflecting a short-term reward estimation. It should be noted that more recent neuroimaging evidence point in favor of a hyper-reactivity of rewards circuitry instead of hypo-reactivity, however, conclusions obtained by the model still holds, as such hyper-reactivity, is accompanied by a bias to immediate rewards [@WCFW3TEU#Stice_Burger_2019]. In line with the reinforcement learning model presented, evidence from probabilistic learning paradigm in obese subjects, shows a decrease impact of negatively valued choices on consequent behavioral adaptation [@PE46B3Z8#Kube_Etal_2018]. This seemingly opposing results can stem from, previously not considered, quadratic associations between BMI and reward sensitivity, where an inverted U-shape is observed and BMI increases [@67GSY6VY#Horstmann_Fenske_Hankir_2015].

Basic reinforcement learning models presented here provide a useful framework to assess the impact of (1) reward sensitivity, (2) learning rates and (3) reward prediction error, more complex models can consider stay/leave behaviors [@6RH6IJB4#Kroemer_Etal_2019], which are part of concurrent decision making. As such, obesity behavior can be characterized for concurrent choices, however, another interesting dimension is decision across different time spans.

### Delayed discouting models

Although the factor determining obesity as an outcome are multiple [@UQ9I8YFE#Ang_Etal_2013], it is reasonable to assume that the more immediate cause is excess intake relative to energetic demands. Moreover, excess of intake is determined in a instance to instance basis, where a decision considering short and long-term benefits/risk must be made. With this in consideration, one can assume that obesity, in part, is caused by sub-optimal short/long-term benefit/risk assessments when taking feeding decisions. If this was the case, as previously noted, areas that are related to compute options value in the short/long term, such as de ACC should be in someway impaired. Delayed discouting referers to the depreciation of a certain reward as function of the time required to obtain it [@9YRMQU6H#DaMatta_Gonçalves_Bizarro_2012], as such, it provides a measures of how reward-related systems bias decision to short or long term. Obese subjects show a robust tendency to steeply discount future rewards [@FCVQ7SB6#Amlung_Etal_2016], thus, favoring short-term rewards. 

Furthermore, ACC, among other structures, shows relative atrophy in obese subjects [@THS94923#Wang_Etal_2017;@5FBDWF55#Raji_Etal_2009], suggesting an impairment of the previously mentioned functions. This findings can be interpreted as if an impairment in environment uncertainty assessment results in a preference for short-term rewards. If this were the case, palatable food sensory cues, which trigger food-intake, would dominate over more, long-term modulated, decisions, such as healthy food intake [@J37T9F5T#Higgs_2016].

Higher future rewards discounting paired with increased motivation to work for food, predict higher caloric intake [@GHWUZPNL#Rollins_Dearing_Epstein_2010], and this effect seems to hold even for low energy-density food [@TLRSYNN6#Epstein_Etal_2014]. The rate of reward discouting, thus, informs about the predisposition to increased energetic intake, independent of possible food-property related effects. Similar effects has been found in children [@8QS2B4AF#Best_Etal_2012] but not in adult males [@IATULRKH#Smulders_Boswell_Henderson_2019]. Moreover, this effects seem to be directly related to body fat [@7B4XUYMB#Rasmussen_Lawyer_Reilly_2010].

## Orexin/Hypocretin system control of foraging

Up to this point, the way reward-related systems interact with environment uncertainty has been discussed. Several structures seem to be involved in integrating reward value in face of environment volatility. Moreover, empirical findings of food-seeking behavior in predictable/unpredictable environments were pointed, however, the direct mechanism that guides food-seeking behavior is lacking. One such system is the Orexin/Hypocretin (HO), which is part of energy homeostatic and feeding pathways [@W3IUQNUY#Toshinai_Etal_2003], and plays a large role in increasing food intake [@5994QM3A#Wolf_2009]. However, a more broad and complex opioid system is thought to control food intake, which in turn is modulated by food preference and selective to certain macro-nutrients, such as fat [@W79GBSE7#Taha_2010]. More recent evidence has linked the activation of hypothalamic HO system to an increase in short-term spatial memory, which is a function that supports exploratory foraging behavior [@28CTMBAN#AittaAho_Etal_2016].

Moreover, orexin promotion of such foraging-related behavior has been postulated as one of its main functions [@FIT9A4HW#Barson_2020]. Such function is relevant because foraging behavior evolved in a specific type of environment, where resources are sparse, clustered and in potential risk of predation, and developed relatively stable strategies to deal with such conditions [@V2XKZN75#Wosniack_Etal_2017]. Thus, foraging behavior, seeks to generate a strategy to maximize energetic intake in a partially known environment, however, if environment resource are non-depleting it can lead to behaviors such as binge eating, finally resulting in excess caloric intake [@FIT9A4HW#Barson_2020].

To provide a connection between food-seeking behavior and uncertainty, evidence on the effects of increasing such uncertainty on the proximal effect of food-seeking behavior, that is, food intake, is neccessary. In that regard, it was pointed that, possibly because of survival mechanisms, environment uncertainty increased food intake and reduced energetic spending. Then, the sufficient functions to support such findings were discussed, emphasizing related structures and functions associated with each on to be accounted by problems with delayed-discounting and ACC atrophy, which points towards a sub-optimal pairing between reward value assignment given environment uncertainty levels. Also, OH system role in foraging was discussed as a proximal cause of overfeeding. Together, this suggests that food-seeking behavior evolved to provide optimal decision-making strategies in uncertain and scarce environments, however, (1) when environment energetic density is high, such strategies would result in overfeeding and (2) obesity in itself can impair homeostatic regulation by altering structures related to uncertainty and reward value processing. Previous points, predict that underlying foraging mechanisms, in certain environments, can lead to obesity.

# Obesogenic environments

# Cafeteria diet and uncertainty

# The decision making problem in obesity

# Conclusions


# References
