import database
import matplotlib.pyplot as plt
import charts

charts.create_bar_chart(database.get_polls_and_votes())
plt.show()