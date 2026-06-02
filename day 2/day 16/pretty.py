from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["pokemon","type"]
table.add_row(["bolt", "nut" ])
table.add_row(["pikachu", "electric" ])
table.add_row(["death", "unavoidable" ])
table.align="l"
print(table)