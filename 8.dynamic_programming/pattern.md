
## 1. Linear/Sequential DP (1D)

```
[?] → [?] → [?] → [?] → [✓]
 ↑     ↑     ↑     ↑     ↑
dp[0] dp[1] dp[2] dp[3] dp[4]

Each state depends on previous states in sequence
```

### Examples

- **Climbing Stairs**: `dp[i] = dp[i-1] + dp[i-2]`
- **House Robber**: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
- **Fibonacci Numbers**
- **Longest Increasing Subsequence (LIS)**
- **Maximum Subarray Sum (Kadane's)**
- **Decode Ways**
- **Word Break**
- **Paint House/Fence**

**Pattern**: `dp[i]` = solution for first i elements

---

## 2. Grid/2D Path DP

```
Start → → → ↓
    ↓   ↘   ↓
    ↓   ↓   ↘
    → → → Goal

dp[i][j] = paths from (i-1,j) ↓ and (i,j-1) →
```

### Examples

- **Unique Paths** (grid navigation)
- **Minimum Path Sum**
- **Dungeon Game**
- **Maximum Square** (in binary matrix)
- **Maximal Rectangle**
- **Cherry Pickup**
- **Triangle** (minimum path sum)

**Pattern**: `dp[i][j]` depends on `dp[i-1][j]` and `dp[i][j-1]`

---

## 3. Interval/Range DP

```
Array: [A, B, C, D, E]
       └─────┘           dp[0][2] = ABC
          └─────┘        dp[1][3] = BCD
       └───────────┘     dp[0][4] = ABCDE

Solve for all possible intervals/ranges
```

### Split-based Examples - **Try all split points**

- **Matrix Chain Multiplication**
- **Optimal Binary Search Tree**
- **Burst Balloons**
- **Minimum Cost to Merge Stones**

### Decision-based Examples -  **Make decisions at endpoints**

- **Longest Palindromic Subsequence (LPS)**
- **Palindrome Partitioning II**
- **Strange Printer**
- **Remove Boxes**

**Pattern**: `dp[i][j]` = solution for range `[i, j]`

---

## 4. Knapsack-type DP

```
Items:    [📦₁, 📦₂, 📦₃, 📦₄]
Values:   [$5, $3, $4, $7]
Weights:  [2kg, 1kg, 3kg, 4kg]

Knapsack: [____10kg____]
          Choose items to maximize value

0/1: Use each item once
Unbounded: Use items multiple times
```

### 0/1 Knapsack Examples

- **Classic 0/1 Knapsack**
- **Partition Equal Subset Sum**
- **Target Sum**
- **Last Stone Weight II**
- **Coin Change (with limited coins)**

### Unbounded Knapsack Examples

- **Coin Change (minimum coins)**
- **Coin Change 2 (combinations)**
- **Rod Cutting**
- **Perfect Squares**
- **Integer Break**

### Bounded Knapsack Examples

- **Backpack with multiple copies**

**Pattern**: Choosing/not choosing items with constraints

---

## 5. String DP

```
String1: A B C D E
         ↓ ↘ ↓ ↘ ↓
String2: A X C Y E

Compare and match characters between strings
dp[i][j] = comparing s1[0...i] with s2[0...j]
```

### Examples

- **Longest Common Subsequence (LCS)**
- **Edit Distance (Levenshtein)**
- **Wildcard Matching**
- **Regular Expression Matching**
- **Distinct Subsequences**
- **Interleaving String**
- **Shortest Common Supersequence**
- **Minimum ASCII Delete Sum**

**Pattern**: `dp[i][j]` compares strings `s1[0...i]` and `s2[0...j]`

---

## 6. State Compression/Bitmask DP

```
Set: {A, B, C, D}
Mask: 1 0 1 1 = {A, C, D} selected
      ↑ ↑ ↑ ↑
      A B C D

Each bit represents presence/absence in set
dp[1011] = solution when {A,C,D} are used
```

### Examples

- **Traveling Salesman Problem (TSP)**
- **Assignment Problem**
- **Subset Sum with tracking**
- **Hamiltonian Path**
- **Minimum Number of Work Sessions**
- **Parallel Courses II**
- **Maximum Students Taking Exam**

**Pattern**: `dp[mask][i]` where mask is a bitmask representing a set

---

## 7. Tree DP

```
        (root)
       /      \
    (L)        (R)
   /   \      /   \
 (LL)  (LR) (RL)  (RR)

Solve bottom-up: leaves → root
dp[node] = f(dp[left], dp[right])
```

### Examples

- **House Robber III** (binary tree)
- **Diameter of Binary Tree**
- **Binary Tree Maximum Path Sum**
- **Longest Path in Tree**
- **Tree Distance Sum**
- **Number of Good Leaf Nodes Pairs**
- **Binary Tree Cameras**

**Pattern**: `dp[node][state]` = solution for subtree rooted at node

---

## 8. Digit DP

```
Build number: _ _ _ _
              ↓ ↓ ↓ ↓
Choices:     0-9 0-9 0-9 0-9
Constraints: (no consecutive 1s, sum ≤ K, etc.)

Build valid numbers digit by digit
```

### Examples

- **Numbers without consecutive 1s**
- **Count of integers with digit sum in range [L, R]**
- **Numbers with at most N given digit**
- **Numbers At Most N Given Digit Set**
- **Count Special Integers**
- **Number of Digit One**
- **Beautiful Numbers**

**Pattern**: Build numbers digit by digit with constraints

---

## 9. Probability/Expected Value DP

```
State transitions with probabilities:
    (i,j) 
   ↙ 0.3 ↓ 0.5 ↘ 0.2
(i+1,j-1)(i+1,j)(i+1,j+1)

dp[i][j] = Σ(probability × next_state)
```

### Examples

- **Knight Probability in Chessboard**
- **Soup Servings**
- **Dice Roll Simulation**
- **New 21 Game**
- **Airplane Seat Assignment Probability**
- **Champagne Tower**
- **Domino and Tromino Tiling** (with probability)

**Pattern**: `dp[i][j]` = probability of state `(i, j)`

---

## 10. Game Theory DP

```
Player A's turn: [1, 5, 3, 7, 9]
                  ↑           ↑
               Pick left   Pick right
               
Player B's turn: [5, 3, 7, 9] or [1, 5, 3, 7]

Optimal play: each player maximizes their advantage
dp[i][j] = max score difference in range [i,j]
```

### Examples

- **Stone Game** (I, II, III, IV variants)
- **Predict the Winner**
- **Nim Game** (and variants)
- **Can I Win**
- **Flip Game II**
- **Guess Number Higher or Lower II**
- **Cat and Mouse Game**

**Pattern**: `dp[i][j]` = max advantage player can get in range `[i, j]`

---

## 🎯 Quick Visual Memory Guide

| Pattern         | Visual Cue     | Remember As                 |
|-----------------|----------------|-----------------------------|
| **Linear**      | `→→→→`         | Dominos falling in sequence |
| **Grid**        | `⬜⬜⬜`<br>`⬜⬜⬜` | Chess board navigation      |
| **Interval**    | `[--range--]`  | Sliding window over array   |
| **Knapsack**    | `🎒+📦`        | Packing a backpack          |
| **String**      | `X\|X\|✓`      | Matching two DNA strands    |
| **Bitmask**     | `1011`         | Light switches on/off       |
| **Tree**        | `🌳`           | Growing from leaves to root |
| **Digit**       | `9️⃣9️⃣9️⃣`    | Building phone number       |
| **Probability** | `🎲`           | Rolling dice outcomes       |
| **Game Theory** | `♟️vs♟️`       | Chess match optimization    |
