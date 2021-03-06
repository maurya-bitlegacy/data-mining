-------------------------
CS685 Assignment 1 ReadMe
-------------------------

1. Files included:

->Shell scripts and json files:

1.1	neighbor-districts-modified.json
1.2	case-generator.sh
1.3	edge-generator.sh
1.4	neighbor-generator.sh
1.5	state-generator.sh
1.6	zscore-generator.sh
1.7	method-spot-generator.sh
1.8	top-generator.sh
1.9	assign1.sh

->.py program files:

1.10	CS685_assign1_ques2.py
1.11	CS685_assign1_ques3.py
1.12	CS685_assign1_ques4.py
1.13	CS685_assign1_ques5.py
1.14	CS685_assign1_ques6.py
1.15	CS685_assign1_ques7.py
1.16	CS685_assign1_ques8.py

->Supporting files (Available at https://api.covid19india.org):
1.17	data-all.json

->Report
----------------------------------------------------------------------------
2. How to run the program?

2.1 	Please install python 3.6 (or higher) using:
		$ sudo apt-get install python3.6

2.2 	Additional python packages needed to be installed:
		pandas - $ pip install pandas
		numpy - $ pip install numpy

2.3 	To run the program from the top, a separate script is provided. Please run assign1.sh. To run some individual program, please run the shell scripts in the top down order as listed in section 1.1 as some programs require supporting files which will be generated by some predecessing program.
		$ ./assign1.sh

2.4 	To run .py programs, please use:
		$ python3 'filename'.py

2.5	To view neighbor-districts-modified.json:
		$ cat neighbor-districts-modified.json

2.6	Dependencies among the programs:

2.6.1	edge-generator.sh uses the file: 
->"mapping.csv" generated by case-generator.sh

2.6.2	neighbor-generator.sh uses the files: 
->"dic_week.json", "dic_month.json", "dic_overall.json", "cases-week.csv", "cases-month.csv" and "cases-overall.csv" generated by case-generator.sh. 
->"district_neighbors.json" generated by edge-generator.sh

2.6.3	state-generator.sh uses the files:
->"mapping.csv", "dic_month.json", "dic_overall.json","cases-week.csv", "cases-month.csv" and "cases-overall.csv" generated by case-generator.sh

2.6.4	zscore-generator.sh uses the files:
->"cases-week.csv", "cases-month.csv" and "cases-overall.csv" generated by case-generator.sh
->"neighbor-week.csv","neighbor-month.csv","neighbor-overall.csv" generated by neighbor-generator.sh
->"state-week.csv","state-month.csv","state-overall.csv" generated by state-generator.sh

2.6.5	method-spot-generator.sh uses the files:
->"dic_week.json", "dic_month.json", "dic_overall.json", "cases-week.csv", "cases-month.csv" and "cases-overall.csv" generated by case-generator.sh
->"neighbor-week.csv","neighbor-month.csv","neighbor-overall.csv" generated by neighbor-generator.sh
->"state-week.csv","state-month.csv","state-overall.csv" generated by state-generator.sh

2.6.6	top-generator.sh uses the files:
->"zscore-week.csv","zscore-month.csv","zscore-overall.csv" generated by zscore-generator.sh

2.7	Known issue on runtime: Some warnings(Divide by 0) will be generated on running zscore-generator.sh. This issue have been inherently fixed in the code by replacing NA with 0.
---------------------------------------------------------------------------
3. Program runtime:

The optimistic runtime of the program when run from the top (assign1.sh) is under 2 minutes. Please allow the kernel to run for this time.
---------------------------------------------------------------------------

Thank you for reading!
@ Author: Sambhrant Maurya
@ Email: samaurya@cse.iitk.ac.in
