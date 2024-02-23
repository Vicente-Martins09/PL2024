import re
 
def markdown_to_html(lines):
    html_output=""
    i=0
    
    while i<len(lines):
        
        if lines[i].startswith("\n"):

            if len(lines[i].strip()) == 0:
                html_output="\n"
            i += 1
        
        elif  lines[i].strip().startswith('#'):
            header_level = lines[i].count('#')
            header_text = lines[i].strip("# ")
            html_output += f"<h{header_level}>{header_text}</h{header_level}>\n"
            i+=1
        
        elif re.match(r"^\s*\d+\.",lines[i]):
            html_output +="<ol>\n"
            while i<len(lines) and re.match(r"^\s*\d+\.",lines[i]):
                html_output += f"<li>{lines[i].strip('1234567890. ')}</li>\n"
                i+=1
            html_output+="</ol>\n"
        #if re.match(r'[1234567890]+\.(.*)')
            
        #markdown = re.sub(r"[1234567890]+\.(.*)",trata_lista,markdown,flags=re.MULTILINE)
        else: 
            #Negrito e Italico
            lines[i] = re.sub(r"\*{2}(.*)\*{2}",r"<b>\1</b>",lines[i].strip())
            lines[i] = re.sub(r"\*{1}(.*)\*{1}",r"<i>\1</i>",lines[i])
            

            #imagem e link
            lines[i] = re.sub(r"!\[(.*)\]\((.*)\)",r'<img src="\2" alt="\1"/>',lines[i])
            lines[i] = re.sub(r"\[(.*)\]\((.*)\)",r'<a href="\2">\1</a>',lines[i])
            html_output += lines[i] + "\n"
            i+=1
    
    return html_output

def main():
    markdown_text = """
    # Título Principal
    ## Subtítulo
    ### Subsubtítulo

    Este é um **exemplo** de *conversão* de Markdown para HTML.
    
    1. Primeiro item de lista ordenada
    2. Segundo item de lista ordenada
    3. Terceiro item de lista ordenada

    Como pode ser consultado em [página da UC](http://www.uc.pt)

    Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
    """
    markdown_lines= markdown_text.split("\n")
    html_output = markdown_to_html(markdown_lines)
    print(html_output)

if __name__ == "__main__":
    main()
