import plotly.express as px
import tkinter as tk

'''
The program calculates how long it takes for a person to become a millionaire by investing a certain amount every month.
Furthermore, it gives her the option to say how long she would maintain this monthly investment rhythm and what her results would be.
By default, a CDB income tax (IR) discount is considered:
    Up to 180 n_days: 22.5%
    From 181 to 360 n_days: 20%
    From 361 to 720 n_days: 17.5%
    More than 721 n_days: 15%
Note: IR is only applied to profit.
IOF is disregarded because time periods tend to be long.
It is assumed that there is no administration fee.
Daily liquidity income is considered to occur only on business n_days (weekends are not considered).
'''

def plot_graphic(x_data, y_data, title=None, x_label=None, y_label=None):
    fig = px.scatter(x=x_data, y=y_data, title=title, template='plotly_dark')
    fig.update_xaxes(title_text=x_label)
    fig.update_yaxes(title_text=y_label)
    fig.show()

def time_for_final_money(final_money, im, monthly_invest, tax):
    '''
    Calculate the time, in n_days, to reach 1 million reais
    Note that the calculated time only takes into account working n_days,
    that is, the real time tends to be longer (adjusted in the code below).
    '''
    i = 0
    curr_value = im
    while curr_value < final_money:
        total_daily_profit = curr_value*tax
        if i <= 180:
            real_profit = total_daily_profit * 0.775
        elif 180 < i <= 360:
            real_profit = total_daily_profit * 0.8
        elif 360 < i <= 720:
            real_profit = total_daily_profit * 0.825
        elif i > 720:
            real_profit = total_daily_profit * 0.85
        
        curr_value += real_profit

        if i % 30 == 0 and i!=0:
            curr_value+=monthly_invest
        i+=1
    return i

def calc_invest(im, monthly_invest, tempo, tax):
    '''
    Calculates and returns the amount resulting from the monthly investment
    during the time period entered by the user.
    '''
    curr_value = im
    days = [0]
    values = [curr_value]
    for i in range(tempo):
        if (i % 6 != 0 and i % 6 != 1) or i < 6 or i % 30 == 0: # Select the day to ensure it is a business day.
            total_daily_profit = curr_value*tax

            if i <= 180:
                real_profit = total_daily_profit * 0.775
            elif 180 < i <= 360:
                real_profit = total_daily_profit * 0.8
            elif 360 < i <= 720:
                real_profit = total_daily_profit * 0.825
            elif i > 720:
                real_profit = total_daily_profit * 0.85

            curr_value += real_profit
            if i % 30 == 0 and i!=0:
                curr_value+=monthly_invest

            days.append(i), values.append(curr_value)

    return (days, values)

def interface():
    info = []

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Investiment information")

    # Define the input fields
    initial_money_label = tk.Label(root, text="Enter how much money you already have:")
    initial_money_label.grid(row=0, column=0, padx=10, pady=5)
    initial_money_entry = tk.Entry(root)
    initial_money_entry.grid(row=0, column=1, padx=10, pady=5)

    monthly_invest_label = tk.Label(root, text="Enter how much you intend to invest monthly: ")
    monthly_invest_label.grid(row=1, column=0, padx=10, pady=5)
    monthly_invest_entry = tk.Entry(root)
    monthly_invest_entry.grid(row=1, column=1, padx=10, pady=5)


    tax_label = tk.Label(root, text="Enter the annual rate of return on the investment (in decimal): ")
    tax_label.grid(row=2, column=0, padx=10, pady=5)
    tax_entry = tk.Entry(root)
    tax_entry.grid(row=2, column=1, padx=10, pady=5)

    years_label = tk.Label(root, text="Enter how many years you plan to continue with this: ")
    years_label.grid(row=3, column=0, padx=10, pady=5)
    years_entry = tk.Entry(root)
    years_entry.grid(row=3, column=1, padx=10, pady=5)

    money_label = tk.Label(root, text="Enter how much money you intend to achieve: ")
    money_label.grid(row=4, column=0, padx=10, pady=5)
    money_entry = tk.Entry(root)
    money_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to retrieve user input
    def submit(output):
        initial_money = initial_money_entry.get()
        monthly_invest = monthly_invest_entry.get()
        tax = tax_entry.get()
        years = years_entry.get()
        expt_money = money_entry.get()

        if not (initial_money and monthly_invest and tax and years):
            print("Please fill in all fields.")
        
        output.extend([initial_money, monthly_invest, tax, years, expt_money])
        root.destroy()

    # Button to submit the input
    submit_button = tk.Button(root, text="Submit", command= lambda: submit(info))
    submit_button.grid(row=6, columnspan=2, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

    return info

def main():
    initial_money, monthly_invest, tax, years, obj_money = interface()

    try:
        obj_money = float(obj_money)
        initial_money = float(initial_money)
        monthly_invest = float(monthly_invest)
        tax = float(tax)/365      # daily yield rate
        n_days = int(years)*365   # number of total n_days
    except ValueError:
        print("Invalid entry. The input needs to be a number.")
    
    n_days, values = calc_invest(initial_money, monthly_invest, n_days, tax) # accumulated value in the time provided with the monthly input accumulation.
    final_value = values[-1]

    n__bus_days = time_for_final_money(obj_money, initial_money, monthly_invest, tax)           # time in n_days that it would take to reach 1 million.
    total_n_days = n__bus_days*365/251                       # n__bus_days only counts the n_days used for income

    inv_report = (
        "===============================================================================================================================\n"
        'INVESTMENT REPORT\n' +
        f'Final value: {final_value:.2f} reais\n' +
        f'You won {(final_value - monthly_invest*(int(years)*12)):.2f} reais with the investment.\n' +
        f'Accumulating {monthly_invest} reais per month and starting with {initial_money} reais, it would take you {(total_n_days/12):.2f} months to reach {obj_money} reais, which would give {(total_n_days/365):.2f} years.'
        "\n==============================================================================================================================="
    )
    print(inv_report)

    n_years = [day/365 for day in n_days]
    plot_graphic(
        x_data=n_years, y_data=values,
        title="Investment plan", x_label="Year", y_label="Amount (reais)"
    )

if __name__ == "__main__":
    main()