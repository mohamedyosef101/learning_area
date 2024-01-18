## What is Reinforcement learning?

A machine learning paradigm where an **agent** (the AI) learn form the **environment** by **interacting with it** (through trial and error) and **receiving rewards** (negative or positive) as a feedback for performing actions.

## The RL process


![***Source**: [The Reinforcement Learning Framework (huggingface.co)](https://huggingface.co/learn/deep-rl-course/unit1/rl-framework)*](https://github.com/mohamedyosef101/101_learning_area/assets/118842452/084e5afa-6168-4138-b9ea-ef6cc17a6d5f)

***Source**: [The Reinforcement Learning Framework (huggingface.co)](https://huggingface.co/learn/deep-rl-course/unit1/rl-framework)*

1. Agent **observes the current state** $S_t$ of the environment *(to get key information about the situation the agent is in).*
2. Based on the state, the agent **selects an action** $A_t$ according to its current policy.
3. The agent executes the action in the environment. *This changes the state of the environment.*
4. The environment **provides a reward** $R_t$ (a numerical value) to the agent based on the consequences of its action. *Positive rewards encourage the agent and negative rewards discourage it.*
5. The agent **updates its policy** based on this feedback to favor actions the produce higher rewards. *This is done by techniques like Q-learning, policy gradient, etc.*
6. The **new state** of the environment is observed and the **process repeated**…

> 🎾 The agent’s goal is to **maximize** its **expected return** (cumulative reward).


### Observations/States

The **information the agent gets from the environment**. In case of video game, it can be a frame (a screenshot). In case of the trading agent, it can be the value of a certain stock, etc.


### Action

The move or decision made by the agent in a given state of the environment.

### Rewards

A signal provided by the environment that conveys feedback to the agent after it executes an action.

### Discounting

Reducing the value of future rewards. We proceed like this: 

1. We define a **discount rate** called ***gamma** $\gamma$.* It must be **between 0 and 1**. *Most of the times 0.95 to 0.99.*
    - The larger the gamma, the smaller the discount. This means our agent **cares more about the long-term reward.**
    - On the other hand, the smaller the gamma, the bigger the discount. This means our **agent cares more about the short term reward (the nearest cheese).**
2. Then, each reward will be discounted by gamma to the exponent of the time step. *Sometimes the future reward will be less and less likely to happen as time goes*.

## Types of tasks

A task is an **instance** of a problem. In RL, we primarily have two types of tasks; **episodic** and **continuous**.

### Episodic task

In this case, we have a **starting** point and an **ending point** (**a terminal state**). This creates an episode: *a list of States, Actions, Rewards, and new States.*

### Continuing tasks

Tasks that **continue forever** (**no terminal state**). *In this case, the agent must learn how to choose the best actions and simultaneously interact with the environment.*

<aside>
🛠 **The Exploration/Exploitation trade-off**

- **Exploration** is *exploring the environment* by **trying random actions to find information** about the environment.
- **Exploitation** is using **known** information to **maximize** the reward.
</aside>

## Two approaches for solving RL problems

In other words, how can we build the RL agent can **select the actions that maximize its expected return** (cumulative reward).

### The Policy $\pi$: the agent’s brain

The Policy **is the function we want to learn**, our goal is to find the **optimal** policy $\pi^*$, *the policy that maximizes expected return when the agent acts according to it*. We find this $\pi^*$ through training.

> There are approaches to find this optimal policy $\pi^*$:
> 
> - **Directly**, by teaching the agent to learn which action to take, given the current state: **Policy-Based Methods.**
> - **Indirectly**, teach the agent to learn which state is more valuable and then take the action that leads to the more valuable states: **Value-Based Methods**.

### Policy-based methods

This function will define a mapping from each state to the best corresponding action. Alternatively, it could define **a probability distribution over the set of possible actions at that state.**

<aside>
🛠 We have two types of policies:

- **Deterministic**: a policy at a given state will always return the same action.
$a\;=\;\pi(s)$
- **Stochastic**: outputs a probability distribution over actions.
$\pi(a|s)\;=\;P[A|s]$
</aside>

### Value-based methods

The value of a state is the **expected discounted return** the agent can get if it starts in that state, and then acts according to our policy.

> “Act according to our policy” just means that our policy is **“going to the state with the highest value”**.
