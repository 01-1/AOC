# Advent of Code - 2023 Solutions
See below the table for some explanations of my strategies!

|   |         |      |     |          |     ||
----|--------:|-----:|----:|----------|-----|-------
Day |     Time| Rank |Score|      Time| Rank| Score
 24 | 00:25:41|  323 |    0|  01:05:18|  112|     0
 23 | 00:22:26|  764 |    0|         -|    -|     -
 22 | 00:17:38|   54 |   47|  00:31:33|  119|     0
 21 | 00:14:39| 1420 |    0|         -|    -|     -
 19 | 00:11:01|  130 |    0|         -|    -|     -
 18 | 00:11:52|  267 |    0|  00:18:03|   59|    42
 17 | 00:23:45|  416 |    0|         -|    -|     -
 16 | 00:11:29|   95 |    6|  00:16:04|  118|     0
 15 | 00:04:35| 1005 |    0|  00:26:07| 1672|     0
 14 | 00:03:56|   77 |   24|  00:14:15|   45|    56
 13 | 00:09:43|  141 |    0|  00:11:53|   51|    50
 12 | 00:12:32|  293 |    0|  00:50:03|  846|     0
 11 | 00:07:39|  211 |    0|  00:12:37|  290|     0
 10 | 00:07:46|   23 |   78|  00:39:37|  140|     0
  9 | 00:02:11|   13 |   88|  00:07:51|  300|     0
  8 | 00:05:39|  594 |    0|  00:18:09|  551|     0
  7 | 00:28:48| 2285 |    0|  00:35:21| 1316|     0
  6 | 00:05:03|  503 |    0|  00:05:48|  187|     0
  5 | 00:12:22|  388 |    0|  01:20:46| 2455|     0
  4 | 00:01:42|   11 |   90|  00:05:19|   25|    76
  3 | 00:46:10| 5294 |    0|  00:50:00| 3408|     0
  2 | 00:10:18| 1349 |    0|  00:11:31|  779|     0
  1 | 00:02:59|  688 |    0|  00:12:21|  646|     0

Some of the code may be modified after submission.

Day 10: excluded due to large file size.

After preprocessing for day 2, I used nvim to replace the bars with the ASCII Box drawing characters as seen in [my ASCII table.](https://gist.github.com/01-1/ba989a502bed38c3cfe48832967b358b)

Then, I used GIMP to flood fill, and manually counted 139 of the squares. I used nvim to select and gedit to count the rest.

Day 11:

First part - generate the grid using transpose, self-explanatory

Second part - just multiply (distance from first part - distance before expansion) * (999999) + distance before expansion

Day 14: My code takes 60 seconds to run with cpython but 6 with pypy :skull:

Remaining days: Might write up solutions later (I probably won't).
