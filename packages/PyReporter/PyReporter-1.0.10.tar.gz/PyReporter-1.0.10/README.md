# [PyReporter](https://github.com/Alex-Au1/PyReporter)
[![PyPI](https://img.shields.io/pypi/v/PyReporter)](https://pypi.org/project/PyReporter)

A Python reporting API that helps with reading and writing tabular data to/from different formats like Excel, SQL tables, etc...


## Install

### Using Pip:
```bash
pip install -U PyReporter
```

## Examples
For more examples, you can go [here](https://github.com/Alex-Au1/PyReporter/tree/main/examples).



#### Writing tables to different sheets in an Excel file

```python
import pandas as pd
import Reporter as rp

view = rp.ReportSubject()

view.attach(rp.ExcelObserver())


data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
data2 = pd.DataFrame({"a": ["cell 1", "cell 2"], "b": ["cell 3", "cell 4"]})
data3 = pd.DataFrame({"catalan": [1, 1, 2, 5, 14, 42, 132]})


# output the number of tables indicated by the sheet name
view.notify(rp.ExcelExportEvent({"Sheet With 1 Table": [rp.ExcelDf(data)],
                                 "Sheet With 2 Tables": [rp.ExcelDf(data), rp.ExcelDf(data2, startcol = 3)],
                                 "Sheet With 3 Tables": [rp.ExcelDf(data), rp.ExcelDf(data2, startcol = 3), rp.ExcelDf(data3, startcol = 6)]} ,"output.xlsx"))

```

<details>
  <summary> Output Result</summary>
    <img width="430" alt="multi_writing2_output1" src="https://user-images.githubusercontent.com/45087631/210030283-c115bd90-d275-434d-bebf-0c8b0df8dc0f.png">
    <img width="419" alt="multi_writing2_output2" src="https://user-images.githubusercontent.com/45087631/210030881-95b756d0-d724-494b-9bdf-50c2acd6b8e2.png">
    <img width="416" alt="multi_writing2_output3" src="https://user-images.githubusercontent.com/45087631/210030885-3e9edebf-a755-49a2-b5e4-bb05d2a5d244.png">

</details>


####  Reading only a portion of a table not centered at A1


<details>
  <summary> Available Files to Read </summary>

  ***input2.xlsx***

  <img width="424" alt="subset_reading_input" src="https://user-images.githubusercontent.com/45087631/210122610-f021696e-019a-482b-ac6e-fd9f94a2f3c5.png">

</details>

```python
import pandas as pd
import Reporter as rp
import asyncio


async def main():
    data_sources = rp.DataSources()
    data_sources["MyInput"] = rp.SourceManager("Only Numbers", "Read Table",
                                               {"Read Table": rp.ExcelSource("input2.xlsx", post_processor = {"full set": rp.DFProcessor(header_row_pos = 1, top = 2, bottom = 7, left = 2, right = 6),
                                                                                                              "subset": rp.DFProcessor(header_row_pos = 1, top = 3, bottom = -1, left = 3, right = -1)})})

    # prints out only the numbers in the table
    output = await data_sources["MyInput"].prepare("subset")
    print(f"-- Subset --\n{output}")

    # prints the full table
    output = await data_sources["MyInput"].prepare("full set")
    print(f"\n-- Full Table --\n{output}")


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()

```

<details>
  <summary> Output Result </summary>

  ```
-- Subset --
1 col 2 col 3
3     1     4
4     2     5
5     3     6

-- Full Table --
1       col 1       col 2       col 3       col 4
2  don't read  don't read  don't read  don't read
3  don't read           1           4  don't read
4  don't read           2           5  don't read
5  don't read           3           6  don't read
6  don't read  don't read  don't read  don't read
  ```
</details>


#### Select a subset of Columns

<details>
  <summary> Available Files to Read </summary>

  ***input4.xlsx***

  <img width="539" alt="select_cols_input" src="https://user-images.githubusercontent.com/45087631/210184631-4031bf11-0665-4a79-8c54-f5bbefbf3a21.png">
</details>

```python
import pandas as pd
import Reporter as rp
import asyncio


async def main():
    data_sources = rp.DataSources()
    data_sources["MyInput"] = rp.SourceManager("Renamed Columns", "Rename",
                                               {"Rename": rp.ExcelSource("input4.xlsx",
                                                                          post_processor = {"original": rp.DFProcessor(header_row_pos = 1, top = 2, bottom = 5, left = 1, right = 7),
                                                                                            "filtered": rp.DFProcessor(header_row_pos = 1, top = 2, bottom = 5, left = 1, right = 7,
                                                                                                                       ind_selected_columns = [0, 2], selected_columns = ["select 3", "repeat"])})})

    # select the correct columns
    output = await data_sources["MyInput"].prepare("filtered")
    print(f"-- Selected Columns --\n{output}")

    # the original table
    output  = await data_sources["MyInput"].prepare("original")
    print(f"\n-- Original Table --\n{output}")


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()

```

<details>
  <summary> Output Result </summary>

  ```
-- Selected Columns --
1             select 1             select 2             select 3
2                    1                    3                    5
3                    a                    c                    e
4  2019-01-20 00:00:00  2019-01-22 00:00:00  2019-01-24 00:00:00

-- Original Table --
1             select 1       don't select 1             select 2       don't select 2             select 3       don't select 3
2                    1                    2                    3                    4                    5                    6
3                    a                    b                    c                    d                    e                    f
4  2019-01-20 00:00:00  2019-01-21 00:00:00  2019-01-22 00:00:00  2019-01-23 00:00:00  2019-01-24 00:00:00  2019-01-25 00:00:00
  ```
</details>
