#CT1 110
#M4t2 
#Robert Crawford
#10/02

#ask the user for a string
#if its one of the tags, print what the tag is and give example of use
#else print ('Tag not found')

def main():

    userTag = input("Enter tag: ")

    if userTag == "p":  
        print("<p> is the paragraph tag.")
        print("Example of use: <p>text</p>")

    if userTag == "h1":  
        print("<h1> defines the most important heading.")
        print("Example of use: <h1>This is heading 1</h1>")

    if userTag == "b":  
        print("<b> tag specifices bold text.")
        print("Example of use: <p>This is <b>bold</b> text.</p>")

    if userTag == "div":  
        print("<div> tag defines a division or a section in an HTML document.")
        print("Example of use: <div style=\"color:#0000FF\"> <p>This is text.</p> </div)")

    else:
        print("Tag not found")
              
main()
              
