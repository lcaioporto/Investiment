# Financial investiment
Python repository that allows the user to evaluate how long it would take to achieve a certain quantity of money by investing monthly.
Furthermore, the program asks the user how long you would maintain this monthly investment, then it prints the final value and shows a graphic detailing the exponential profit growth.

By default, a CDB income tax (IR) discount is considered:
<p>
     Up to 180 days: 22.5%;
</p>
<p>
     From 181 to 360 days: 20%;
</p>
<p>
     From 361 to 720 days: 17.5%;
</p>
<p>
     More than 721 days: 15%.
</p>
Note: IR is only applied to profit.

IOF is disregarded because time periods tend to be long.
It is assumed that there is no administration fee.
Daily liquidity income is considered to occur only on business days (weekends are not considered).
<p>
     It is important to highlight that the program presents an approximate and not entirely realistic result, as the IOF and possible rate fluctuations that may occur over the years are disregarded.
</p>

# Application example

The program must be run in the terminal. Then, a window will appear asking for information about the investment:
<p>
<img width="710" alt="image" src="img\img1.png">
</p>

You must provide information about all the parameters and then click on "Submit".
When the program finishes successfully, a pop-up window will be shown with the investiment report:
<p>
<img width="710" alt="image" src="img\img2.png">
</p>

Besides that, a graphic will be shown:
<p>
<img width="710" alt="image" src="img\img3.png">
</p>