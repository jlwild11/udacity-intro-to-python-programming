def html_list(list):
    html = ["<ul>"]
    for string in list:
        html.append("<li>{}</li>".format(string))
    
    
    html.append("</ul>")
    html = "\n".join(html)
    return html
    
list1 = ['first string', 'second string','third string']  
print(html_list(list1))