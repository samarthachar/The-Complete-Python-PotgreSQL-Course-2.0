import matplotlib.pyplot as plt

def create_pie_chart(options):
    print("DEBUG OPTIONS:", options)
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)

    axes.pie(
        [int(option[1]) for option in options],
        labels=[option[0] for option in options],
        autopct="%1.1f%%"
    )
    return figure