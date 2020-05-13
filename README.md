# Surf-Up
Using **Python, SQLAchemy, and Flask**, to analyze and visualize climate date as preparing to open a surf shop.<br>

## Steps
•	Explain the structures, interactions, and types of data of a provided dataset.<br />
•	Differentiate between SQLite and PostgreSQL databases.<br />
•	Use **SQLAlchemy** to connect to and query a **SQLite** database.<br />
•	Use statistics like minimum, maximum, and average to analyze data.<br />
•	Design a **Flask** application using data.

## Discussion
•	Compare your statistical findings between the month of *June* and *December*.<br />
1. The mean, max, and min temperatures in June all are higher than December. 
2. The std of June is lower than December, indicating values are also closer to the mean.<br />

•	Make 2 or 3 recommendations for further analysis.
1. Besides temp, prcp should be looked into as well, since prcp is important (better not too much and not too less).
2. Other than june and dec, other monthes should be also included, so we could have other data to compare with.<br />

•	Share your findings in the *Jupyter Notebook*.<br />

&nbsp;&nbsp;&nbsp;&nbsp;Sep:&nbsp;&nbsp;Mean Temp 77.7 and Mean Prcp 0.28 <br />
&nbsp;&nbsp;&nbsp;&nbsp;Dec:&nbsp;&nbsp;Mean Temp 71.1 and Mean Prcp 0.20 <br />
&nbsp;&nbsp;&nbsp;&nbsp;Mar:&nbsp;&nbsp;Mean Temp 72.4 and Mean Prcp 0.17 <br />
&nbsp;&nbsp;&nbsp;&nbsp;June:&nbsp;Mean Temp 77.2 and Mean Prcp 0.12 <br />

1. The Temp reaches the highest on Sep, and then drops on Dec.
2. The Prcp remains the highest on Sep, and then keeps droping until June. 

3. In June, even the Prcp is low, but prcp was high since Sep to Dec, the environment should be green to attract travellers for surfing and ice cream along with high temp.
4. In Dec, since the temp is lower and Prcp is higher, maybe less ppl come to surfing...Hopefully, the holiday season could bring more travellers for ice cream.
5. Btw Dec n June, the Temp is getting higher and prcp is getting less, the environment should be getting better for surfing.
6. Btw June n Sep, the Temp remains high but way more Prcp, possibly more people stays indoor for ice cream.

---
The codes are in `climate_analysis.ipynb` and `flask_example.py`

