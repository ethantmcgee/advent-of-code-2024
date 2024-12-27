# Advent of Code

This solution contains my 2024 Advent of Code solutions.  An overview of the solutions along with my estimation of each day's difficulty is provided below.  All solutions are released under an [MIT License](LICENSE).

I have denoted where I looked up hints in the descriptions below.

## Day 1

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 2

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 3

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 4

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 5

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 6

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 7

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 8

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 9

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 10

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 11

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 12

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 13

Difficulty: X/5 (Part 1), X/5 (Part 2)

Overview: TBW

## Day 14

Difficulty: 2/5 (Part 1), 3/5 (Part 2)

Overview: Part 1 is just simulate the movements, and then break the robots into a quadrant.  For part 2, I just generated 5000 steps, then looked for lines in the file that had 9 1s in a row using a regex.  That found the step pretty quickly after the generation finished.

## Day 15

Difficulty: 2/5 (Part 1), 4/5 (Part 2)

Overview: Part 1 is just a direct simulation with a little recursion.  Part 2 I took a more math oriented approach where I instead used recursion to find what boxes could be affected.  Then I checked to ensure the boxes could move.  If so, I applied a transformation on all boxes.

## Day 16

Difficulty: 3/5 (Part 1), 3/5 (Part 2)

Overview: I sorta solved part 2 while solving part 1 since my part 1 solution actually returned the path followed to the output.  Both solutions use a heapmap to continuously branch off the currently known lowest score.

## Day 17

Difficulty: 1/5 (Part 1), 4/5 (Part 2)

Overview: Part 1 is just a simulator, no real tricks.  Part 2 required doing a bit of reading on [Reddit](https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2hunb8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) to realize that the each pair of 3 bits controlled an output.  Once that was realized, you can just run a search over the input space and check the results each time to see if it matches what you expect.

## Day 18

Difficulty: 1/5 (Part 1), 4/5 (Part 2)

Overview: For part 1, lay out 1024 steps, and then run a BFS.  For part 2, I used brute force.  Lay out 1025 steps, see if there is a solution, if yes, increment to 1026, and recheck.  Keep going until no solution exists.  Not a pretty approach but it worked.

## Day 19

Difficulty: 1/5 (Part 1), 3/5 (Part 2)

Overview: Wound up solving this one on part 1 more or less as I actually counted the number of combinations (I was guessing that would be relevant in part 2 and was happily right).  For part 1, add 1 if count is > 1.  For part 2, just sum the counts.

## Day 20

Difficulty: 3/5 (Part 1), 4/5 (Part 2)

Overview: Part 1 can be done with brute force.  You simply change each # to a . and then check to see if it saves you time by doing a BFS.  This does not scale for part 2.  For part 2, I wound up using [Manhattan distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html), and effectively walking along my BFS discovered path, for each step, I looked into the future to see if there was a point that was within 20 manhattan steps of my current point that saved time.  Both problems had some minor rules that had be encoded into the solution regarding what counted as saving time.

## Day 21

Difficulty: 4/5 (Part 1), 4/5 (Part 2)

Overview: This is one of those days that I wasn't sure where to even start. I found a solution on [Reddit](https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m35h3a8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) that clicked and made me realize this is just a divide / conquer problem with caching.  My approach wound up being very similar with some differences due to varied input.

## Day 22

Difficulty: 1/5 (Part 1), 3/5 (Part 2)

Overview: You're provided the formula for part 1, just convert it directly to code.  Part 2 was a little trickier, but you can actually solve the problem with a single scan over the input by just keeping the last 4 differences.  If you simulate every possible 4 tuple of changes as you iterate, you can just pick the biggest result at the end.

## Day 23

Difficulty: 2/5 (Part 1), 4/5 (Part 2)

Overview: Very simple input parsing today.  Part 1 is a 3-clique finder, nothing fancy.  Part 2 is an NP-Hard problem today!  You want to find the maximum clique in a graph.  I was a bit lazy here.  I decided, eh, let's find a 3 clique then spider out from the 3 clique expanding it as much as we can.  I figured that we would probably find a clique that covered most of the graph, and we could just skip checking any other nodes that were already in that massive clique.  This approach worked rather nicely as there was a massive clique that covered most of the graph.  This approach would not work well if the biggest clique was in a rather small section of the graph.

## Day 24

Difficulty: 1/5 (Part 1), 5/5 (Part 2)

Overview: Part 1 is a rather simple boolean logic simulator which requires a couple passes over the input as values arrive at new wires.  Part 2, yeah I had no clue what I was looking at.  I found a beautiful explaination on [Reddit](https://www.reddit.com/r/adventofcode/comments/1hla5ql/2024_day_24_part_2_a_guide_on_the_idea_behind_the/) that demonstrated that the input was actually a [Ripple Carry Adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder).  Within the comments, [there is a rule based approach that allows you to find the incorrect wires with two passes over the input](https://www.reddit.com/r/adventofcode/comments/1hla5ql/comment/m3lh9un/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).

## Day 25

Difficulty: 1/5 (Part 1), N/A (Part 2)

Overview: Honestly the worst part of this day is just parsing the input.  After that its a simple double for loop just checking to see if the sum of the lock column and the key column is greater than 6.
