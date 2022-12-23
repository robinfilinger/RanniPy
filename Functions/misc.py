from table2ascii import table2ascii as t2a, PresetStyle

#header=["ID", "Name", "Type", "Birthday", "Age", "Nature", "Owner", "FavFood"],
def toTable(inHeader, inBody):
    output = t2a(
    header= inHeader,
    body= inBody
    )
    return output

