# Title

- 'Role of orexin and opioid dynorphin peptides in food intake and obesity'
- 'Real-time centroid calculation for behavioral experiments'

# Laboratory and tutor

- Claudio Perez Leighton

# General question

- What's the difference in the effect of dynorphin and orexin in hedonic intake, between preferred and non-preferred food?
- This can be in a 'elasticity' measurement scenario
- or Free behavior scenario

# Theory (brief)

- Orexin neuropeptide that regulates aoursal, wakefulnes, feeding behavior, they are made exclusively by hypothalamic neurons and have extensive projection trough the central nervous system

- Dynorphin related to homeostatic feeding, stress response, exerts their effects through k-opioid receptor

- Homeostatic feeding: given and energy depletion, this is characterized by an increased motivation to eat and restore energy balance

- Hedonic feeding: augment in feeding motivation, with no energy deficit, particulary in highly palatable foods

- Palatable: has multiple defintions, but are foods which on consumption increases the intake or are largely preferred

- In reward circuits (ventral tegmental area) -> OXA increases hedonic intake

- In reward circuits (ventral tegmental area) -> DYN block OXA effect

- In PVN (paraventricular hypothalamic nucleus) the effects are reversed

- Both OXA and DYN have site-specific effects

- Blockade of orexin (in ventral pallidum) -> increased elasticity (in drug seeking behavior)

- Exendin-4 (inhibits food intake) and this effects if modulated by food preference (preferred food 'blocks' exendin-4 effect)

# Hypothesis

- Determine whether opioid DYN and orexin in PVN have opposing effects on hedonic intake
- That is: prefered vs non-prefered
- Elasticity given punishement to preferred tasty food
Price elasticity of demand
- DYN en PVN -> enhances hedonic intake: más elástico
- OXA en PVN -> blocks hedonic intake: poco elástico
- ad libitum
# General objectives

- Important measures in this kind of experiments are spontaneus physical activity, measures of selection conflict, among others, all of which need to have x, y, z data of mice. Also to evaluate elasticity we need to measure 'licks'

- Objective 1: using python opencv generate a 'workflow' that is automated enough to control multiple instances
- Objective 2: for each instance, generate a script that allows to generate, in real time, processing of x, y, z coordinates and centroid calculation
- Objective 3: for each instance, generate a script that can manage adequately both data and video recordings

# Methods

- Currently no relevant data to re-analyze
- Segmentation algoritms (fast enough to operate in a pi)
- Centroid calculation (the challenge is head movement)
- Sync 'licks' with centroid position y the proper time scale
- Possibly -> calculation of spa and conflict (deviation from optimal path)
