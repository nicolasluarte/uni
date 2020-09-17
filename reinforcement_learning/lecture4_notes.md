# model-free prediction

## introductionm

- estimate the value function of an **unknown** MDP

## monte-carlo learning

- figure out the values, without having environment dynamics
- value = mean return
- you have to terminate in order to form the mean
- all episodes must terminate
- lean the value from episodes of experience under policy pi
- returns are total discounted reward
- in montecarlo we use empirical mean return instead of expected return

### first visit monte-carlo policy evaluation

- count number of visit
- add total return
- obtain mean return from first visit only
- law of large numbers, mean converges to true expectation
- reachable states under a given policy, is not a full policy

### every visit monte-carlo policy evaluation

- we consider every visit to each state

- for non-stationary environment, we can change the step size to forget previous rewards

## temporal-difference learning

- learn directly from actual experience
- model-free
- bootstrapping
- immediate reward plus discounted value of the next step
- TD target
- TD error

## TD lambda

- it gives a way to move between monte-carlo and TD
