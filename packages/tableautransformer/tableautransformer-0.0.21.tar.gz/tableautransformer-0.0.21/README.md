# TableauTransformer
======

ETL tooling for preparing tableau seed data

## Description

This library was built with the intentions of enhancing the experience of data wrangling for tableau.
Tableau can be very particular about the data it reads from.
In addition preparing data to fit the shape for different graphs can be time consuming.
TableauTransformer can be used to hurdle over these two barriers.

## Dependencies

* pip, python 3.6, pandas, numpy

## Getting Started

```
pip install tableautransformer
```

```
import tableautransformer as tbt
```

tbt is a collection of functions, not a collection of methods, so all calls are "tbt.function_name()"

## Function Docs

Here you can find a list of all functions within the library, a description of what they do, and their inputs.

### Basic_Table()

```
basic_table(read_path, read_type='csv', sheet_name=None, columns_to_keep=None, columns_rename=None, 
                filters=None, group_by=None, aggregate_columns=None, pre_agg_math_columns=None, 
                post_agg_math_columns=None, remove_NAN=True, remove_NAN_col='all')
```

##### Description

basic_table is the basis for the tbt library as it refactors ~20 lines of commonly repeated code down to one input heavy function. The function reads in a dataframe, cleans up the data, and performs commonly used table operations.

##### Inputs

> read_path: string
>> The path to the file you wish to read. The only mandatory input.

> read_type: 'csv' or 'excel'
>> Default is csv, if type is excel then sheet_name must have a value.

> sheet_name: string
>> The name of the tab you wish to read in.

> columns_to_keep: list of strings
>> ['colA','colB','colC'] This function runs immediately after reading in the data, any column mentioned in the list will remain in the dataframe, all others are dropped.

> columns_rename: list of strings
>> ['colA','colB','colC'] the renaming process occurs after the file is read in and columns_to_keep have been selected. All other column related inputs should use the new name dictated by the rename process.

> filters: list of 3-element tuples
>> [('col_name','operand','value')] the input can be multiple filters, each filter is a 3-element tuple where the first element is the column name, the second is the operand, and the third is the value. The column name and operand must be strings while the value can be numeric (or a string if the operand is '==').

> group_by
>>

> aggregate_columns
>>

> pre_agg_math_columns
>>

> post_agg_math_columns
>>

> remove_NAN
>>

> remove_NAN_col
>>

***

### Bucket()

```
bucket(df, column, bucket_col_name, intervals)
```

##### Description

##### Inputs

***

### Is_In()

```
is_in(df, target_col, isin_list)
```

##### Description

##### Inputs

***

### Cast()

```
cast(df, target_col, value)
```

##### Description

##### Inputs

***

### Date_Format()

```
date_format(df, target_col, date_format)
```

##### Description

##### Inputs

***

## Authors

Contributors names and contact info

* Josh Teixeira  |  jteixeira@cppib.com

## Version History

* 0.0.17
    * README documentation enhanced
* 0.0.16
    * bucket function added
* 0.0.1
    * Initial beta release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details