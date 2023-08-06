# scpQCA

scpQCA is a new and more powerful algorithm. QCA(Qualitative Comparative Analysis), a kind of configurational comparative method, follows after [Ragin](https://books.google.com/books?hl=zh-CN&lr=&id=PnI-DQAAQBAJ&oi=fnd&pg=PP1&dq=QCA+Ragin&ots=ZLKBNEMpEy&sig=Kg9oQrTzez3HkMguKEUOaAtCXEw).

The source code could find in https://github.com/Kim-Q/scpQCA.git, please obey the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.html) license.

Here follows the tutorial of scpQCA:

## a common usage of scpQCA

### `scpQCA`(data: dataframe, decision_name:str, caseid: str)

```
import scpQCA
import pandas pd

data=[[random.randint(0,100) for _ in range(6)] for _ in range(30)]
data=pd.DataFrame(data)
data.columns=['A','B','C','D','F','cases']
obj=scpQCA.scpQCA(data,decision_name='F',caseid='cases')
```

To make scpQCA get rid of the uneven sample distribution problem, `data `after deduplication services better than the dataset with many repeated cases. Use `drop_duplicates` process before establishing a scpQCA model.

More than this, `data `should also check the `dropna `function or the program will alert the errors.

### `indirect_calibration` (feature_list: list of column names, class_num: int, full_membership: float, full_nonmembership:float)

If calibration is needed, scpQCA provides two kinds of calibration functions `direct_calibration `and indirect_calibration.

```
feature_list=['A','B','C','D','F','cases']
obj.indirect_calibration(feature_list,2,100,0)
```

### `direct_calibration `(feature_list: list of column names, full_membership: float, cross_over: float, full_nonmembership: float)

### `raw_truth_table `(decision_label: unique, feature_list: list of column names, cutoff: int, consistency_threshold: float, sortedby: bool)

To make the process visualization, you can use `raw_truth_table `or `scp_truth_table `to print some key results.

```
obj.raw_truth_table(decision_label=1, feature_list=feature_list, cutoff=1,consistency_threshold=0.6,sortedby=False)

###
      A    B    C    D  number            caseid  consistency  coverage
0  0.0  0.0  1.0  1.0       4  [69, 47, 27, 58]     1.000000  0.210526
1  1.0  0.0  0.0  0.0       2          [13, 89]     1.000000  0.105263
2  1.0  0.0  1.0  1.0       2          [41, 10]     1.000000  0.105263
3  1.0  0.0  0.0  1.0       1              [31]     1.000000  0.052632
4  0.0  1.0  1.0  0.0       1             [100]     1.000000  0.052632
5  1.0  1.0  1.0  0.0       4  [96, 69, 75, 33]     0.750000  0.157895
6  0.0  0.0  0.0  1.0       3      [84, 73, 14]     0.666667  0.105263
```

### `scp_truth_table `(rules: list of candidate rules, feature_list: list of column names, decision_label: unique)

However the scpQCA's candidate rule list should run after the sufficiency analysis(`candidate_rules`):

```
obj.scp_truth_table(rules, feature_list=feature_list,decision_label=1)

###
Running...please wait. There are 16 factor combinations.
There are 13 candidate rules in total.
      A    B    C    D  number consistency coverage
0     -    -  1.0    -      14      0.6429   0.5294
1     -  0.0    -    -      15      0.6000   0.5294
2     -  0.0    -  1.0       9      0.7778   0.4118
3     -  1.0    -  0.0      10      0.7000   0.4118
4     -  0.0  1.0    -       7      0.7143   0.2941
5     -    -  1.0  0.0       8      0.6250   0.2941
6     -  0.0  1.0  1.0       4      1.0000   0.2353
7     -  1.0  1.0  0.0       5      0.8000   0.2353
8     -    -  1.0  1.0       6      0.6667   0.2353
9     -  0.0  0.0  1.0       5      0.6000   0.1765
10    -  1.0  0.0  0.0       5      0.6000   0.1765
11  0.0  0.0  1.0  1.0       1      1.0000   0.0588
12  0.0    -  1.0  1.0       1      1.0000   0.0588
```

### `search_necessity `(decision_label: unique, feature_list: list of column names, consistency_threshold: float)

`Feature_list `shouldn't contain any symbol or blank space, while '_' in the middle is allowed. `Feature_list `counld contain `decision_name ,` `caseid `or neither.

Pay attention to the special parameter `consistency_threshold`, it usually takes approximately 0.9.

```
obj.search_necessity(decision_label=1, feature_list=feature_list,consistency_threshold=0.8)

###
B==1.0 is a necessity condition
C==1.0 is a necessity condition
```

### `candidate_rules `(decision_label: unique, feature_list: list of column names, consistency: float, cutoff: int)

`Feature_list `shouldn't contain any symbol or blank space, while '_' in the middle is allowed. `Feature_list `counld contain `decision_name ,` `caseid `or neither.

Pay attention to the special parameter `consistency_threshold`, it usually takes the lower limit of 0.75; parameter `cutoff`, it usually takes the lower limit of 2.

```
rules=obj.candidate_rules(decision_label=1, feature_list=feature_list, consistency=0.8,cutoff=1)
```

### `greedy `(rules: list of candidate rules, decision_label: unique, unique_cover: int)

The rules input is the output of `candidate_rules`.

Pay attention to the special parameter `unique_cover`, it should be set smaller than `cutoff `in `candidate_rules `and makes a big impact on final solution.

```
configuration,issue_set=obj.greedy(rules=rules,decision_label=1,unique_cover=2)
print(configuration)
print(issue_set)

###
A==0.0 is a necessity condition
Running...please wait. There are 16 factor combinations.
There are 27 candidate rules in total.
['B==0.0 & A==0.0', 'D==1.0 & A==0.0', 'D==0.0 & C==0.0 & A==0.0']
{5, 8, 10, 12, 13, 17, 20, 22, 23, 24, 26, 28}
```

### `con_n_con `(decision_label: unique, configuration: list of candidate rules, issue_sets: set of caseid)

`configuration `and `issue_sets `are the calculated from `greedy`.

```
obj.cov_n_con(decision_label=1, configuration=configuration,issue_sets=issue_set)

```

```
OUTPUT：

###
consistency = 0.6 and coverage = 0.7058823529411765
```

### `runQCA `(decision_label: unique, feature_list: list of column names, necessary_consistency: list, sufficiency_consistency: list, cutoff: list, rule_length: int, unique_cover: list)

Otherwises, we also recommand you to use a more convenience function to test the best parameters.

```
data=[[random.randint(0,100) for _ in range(6)] for _ in range(30)]
data=pd.DataFrame(data)
data.columns=['A','B','C','D','F','cases']
<<<<<<< Updated upstream
obj=scpQCA(data,decision_name='F',caseid='cases')

feature_list=['A','B','C','D','F','cases']
obj.indirect_calibration(feature_list,2,100,0)

configuration,issue_set=obj.runQCA(decision_label=1, feature_list=feature_list, necessary_consistency=[0.8,0.9],sufficiency_consistency=[0.75,0.8],cutoff=[1,2],rule_length=5,unique_cover=[1])

print(configuration)
print(issue_set)
print(obj.cov_n_con(decision_label=1, configuration=configuration,issue_sets=issue_set))
=======
obj=scpQCA.scpQCA(data,decision_name='F',caseid='cases')

feature_list=['A','B','C','D','F','cases']
obj.indirect_calibration(feature_list,2,100,0)

configuration,issue_set=obj.runQCA(decision_label=1, feature_list=feature_list, necessary_consistency=[0.8,0.9],sufficiency_consistency=[0.75,0.8],cutoff=[1,2],rule_length=5,unique_cover=[1])

print(configuration)
print(issue_set)
print(obj.cov_n_con(decision_label=1, configuration=configuration,issue_sets=issue_set))
```

```
OUTPUT：
>>>>>>> Stashed changes

###
Running...please wait. There are 16 factor combinations.
There are 20 candidate rules in total.
processing the simplification with para: necessary consistency=0.8, sufficiency consistency=0.75, cutoff=1, unique cover=1
consistency = 0.7894736842105263 and coverage = 0.9375
processing the simplification with para: necessary consistency=0.8, sufficiency consistency=0.75, cutoff=2, unique cover=1
consistency = 0.7894736842105263 and coverage = 0.9375
processing the simplification with para: necessary consistency=0.8, sufficiency consistency=0.8, cutoff=1, unique cover=1
consistency = 0.8666666666666667 and coverage = 0.8125
processing the simplification with para: necessary consistency=0.8, sufficiency consistency=0.8, cutoff=2, unique cover=1
consistency = 0.8666666666666667 and coverage = 0.8125
processing the simplification with para: necessary consistency=0.9, sufficiency consistency=0.75, cutoff=1, unique cover=1
consistency = 0.7894736842105263 and coverage = 0.9375
processing the simplification with para: necessary consistency=0.9, sufficiency consistency=0.75, cutoff=2, unique cover=1
consistency = 0.7894736842105263 and coverage = 0.9375
processing the simplification with para: necessary consistency=0.9, sufficiency consistency=0.8, cutoff=1, unique cover=1
consistency = 0.8666666666666667 and coverage = 0.8125
processing the simplification with para: necessary consistency=0.9, sufficiency consistency=0.8, cutoff=2, unique cover=1
consistency = 0.8666666666666667 and coverage = 0.8125
The best opt parameter of scpQCA is: necessary consistency=0.8, sufficiency consistency=0.75, cutoff=1, unique cover=1
['C==0.0 & B==0.0', 'D==0.0 & A==1.0', 'C==1.0 & B==1.0 & A==1.0', 'D==0.0 & C==1.0 & B==1.0', 'D==1.0 & C==0.0 & A==0.0']
{1, 4, 7, 8, 9, 10, 11, 14, 15, 17, 20, 25, 26, 28, 29}

```

The input of `necessary_consistency`, `sufficiency_consistency`, `cutoff` and `unique_cover` are `list` datatype. Function will find the best parameter combination and output the one.
