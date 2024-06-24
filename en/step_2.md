## When life gives you lemons, make lemonade

Let's start by asking the player to choose how many glasses of lemonade to make.

--- task ---

Open a new empty Scratch project.

[[[generic-scratch3-new-project]]]

--- /task ---

--- task ---

Add a backdrop with an outdoor landscape. 'Blue Sky' is a good choice.

![screenshot](images/lemonade-stage.png)

[[[generic-scratch3-backdrop-from-library]]]

--- /task ---

--- task ---

Add code to ask the player a question.

```blocks3
when green flag clicked
ask [How many glasses of lemonade should I make?] and wait
```

--- /task ---

Having asked your player to make a choice, you'll need somewhere to store the answer. To do that you'll need a variable.

Create a new variable called `lemonade`{:class="block3variables"}.

[[[generic-scratch3-add-variable]]]

Now set this variable to the answer block after asking your question.

--- hints ---
--- hint ---

```blocks3
set [lemonade v] to (answer)
```

--- /hint ---
--- /hints ---

--- task ---

Lets assume we have 100 potential customers passing your stand each day, and each one has a 30% chance of buying a glass of lemonade. How can we model this in our game?

Create a second variable and call this one `sales`{:class="block3variable"}.

Can you add code to set this variable to the number of glasses of lemonade bought?

--- hints ---
--- hint ---

For each potential customer we need to randomly decide if they want to buy a glass of lemonade and if we have any left.

--- /hint ---
--- hint ---

Here are some blocks you might find useful:

```blocks3
set [sales v] to (0)

repeat (100)
end

if < > then
end

< > and < >

[ ] < [ ]

[ ] > [ ]

pick random (0) to (99)

(lemonade)

change [sales v] by (1)

change [lemonade v] by (-1)
```

--- /hint ---
--- hint ---

Your code might look like this:

```blocks3
when green flag clicked
ask [How many glasses of lemonade should I make?] and wait
set [lemonade v] to (answer)
set [sales v] to (0)
repeat (100)
    if < < (pick random (0) to (99)) < (30) > and < (lemonade) > (0) > then
        change [sales v] by (1)
        change [lemonade v] by (-1)
    end
end
```

--- /hint ---
--- /hints ---

--- /task ---
