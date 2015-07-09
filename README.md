# housing_model

This is an agent based model of the housing market. It is made to demonstrate the effect of adding high-end housing units on the number and demographics of renters displaced.

Here is a presentation of the model: https://docs.google.com/file/d/0B6FpfcltJScFaFdrS3FMRWlXanc/edit

## Getting started

Make sure you have [python](https://www.python.org/downloads/) and [git](https://help.github.com/articles/set-up-git/)

In terminal:

```
> git clone https://github.com/SonjaKT/housing_model.git
> cd housing_model/
> python simulate.py

```
Enter the number of renters and housing units at each of the 5 levels for your model. Note that, for now, there must be more people than houses for each level.
```
input number of renters with minimum housing score 1: 10
input number of renters with minimum housing score 2: 15
 ...etc
```
The model will match the renters to units. This may take a minute or two, especially when modeling 1000s of renters and units. Smaller numbers of renters and units will finish more quickly.


## How it works

## Agents, Mechanics of Model

The agents called "renters" have the following attributes:
 1. Ability (or willingness) to pay: lognormal distribution of real numbers (0, infinity); mean ability to pay is $2200

 2. Minimum housing standard constraint.
This variable reflects a renter's subjective preference for "niceness", or proximity to transit, or size. This is a whole number from 0 to 4. Standard constraints are distributed uniformly.
A single person who requires a new unit with luxury amenities and can't live with roomates will have score 4, as will a family of 6 who would accept a unit of any age, in any type of neighborhood, with any level of access to amenities.

The agents called "houses" have the following attributes:
1. Housing standard score.
This is a whole number from 0 to 4. 
Initially, This score is distributed “normally.” Most homes are 2s, the next most common are 1s and 3s, the rarest are 0s and 4s.

## Parameters

We ran two experiments.
In one we have a housing unit: renter ratio of 2:3. For every 3 potential renters there are only 2 housing units available. The distribution of housing types is “normal,” as described above. 

In the 2nd experiment, the housing unit:renter ratio is 2.5:3, with all of the new units added in the highest “quality” category. All of the new units are “4”.

In each experiment, renters “view” 20 houses randomly selected from the pool of houses. All houses start with a rent of $100. Each renter enters a bid for her most preferred house, assuming she can afford 5% higher than the current rent. If the bidding on the house exceeds what she is able to pay, she begins bidding on her second-most preferred house, and so on. This proceeds until all houses are filled; since there are more renters than houses, some renters will be displaced from the market. This algorithm creates a “stable matching”: while not every renter is guaranteed to have his most preferred house, there will be no two renters who would be willing to trade places with one another, given the current rent prices.
 
## Results
In each experiment, the most displaced people are the ones with highest standard constraints and lowest income. 

Comparing experiment one and experiment two:
Adding housing reduced the raw number of renters displaced. 
[Demographic of displaced renters comparison under 2 scenarios]
[Rent distribution comparison under 2 scenarios]

## What's next for Housing Market Model
Add complexity:
Houses could have a minimum rent accepted. This would reflect the landlord's willingness to have a tenant. Currently in the model all landlords will accept a tenant at any price. In reality, there are landlords who don't need to rent out their units for financial reasons, and are willing to allow them to stay empty rather than rent them below some idiosyncratic price.
Allow for different types of pricing models (e.g. rent control)

Add interactivity and visualization:
Run the model in the browser. Allow users to adjust parameters and visualize results.
