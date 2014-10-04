"""
html_render.py Python class example.

a simple set of classes for rending html.

Used to demonstrate simple subclassing, attribute and method overriding, etc.

"""


class Element(object):
    """
    An element with optional attributes and multiple items in the content.
    """
    tag = u"html" # just so there is default
    indent = u"    "
    def __init__(self, content=None, **kwargs):
        """
        initialize an element with optional attributes, and any number
        of sub-elements and content

        :param content: content of the element:  single string or another Element.
                        an empty string will be ignored
        :param [kwargs]: optional attributes as keyword parameters.

        """
        if not content:  # will catch None and empty string
            self.children = []
        else:
            self.children = [content]

        self.attributes = kwargs

    def append(self, element):
        """
        add som more content to the Element, could a simple string or
        an Element object.
        """
        self.children.append(element)

    def render(self, file_out, ind=u""):
        """
        render this element, including attributes
        """
        file_out.write(u"\n")
        file_out.write(ind)
        file_out.write(u"<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(u' %s="%s"'%(key, value) )
        file_out.write(u">")
        for child in self.children:
            try:
                child.render(file_out, ind + self.indent)
            except AttributeError: # Assume it's a string or unicode object
                                   #   if it doesn't have a render method
                file_out.write(u"\n")
                file_out.write(ind + self.indent)
                file_out.write(unicode(child))
        file_out.write(u"\n")
        file_out.write(ind)
        file_out.write(u'</%s>'%self.tag)


class Html(Element):
    tag = u"html"

    ## override the render method to add the "<!DOCTYPE html>"
    def render(self, file_out, ind=u""):
        print u"in Html render method"
        file_out.write(u"<!DOCTYPE html>")
        # call the superclass render:
        Element.render(self, file_out, ind)


class Head(Element):
    tag = u"head"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"


class SelfClosingTag(Element):
    """
    Element with a single tag -- no content, only attributes
    """
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, ind=u""):
        """
        an html rendering method for self-closing elements:
        attributes, but no content a no closing tag

        ( may not be XHTML compliant...)
        """
        file_out.write(u"\n")
        file_out.write(ind)
        file_out.write(u"<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(u' %s="%s"'%(key, value) )
        file_out.write(u" />")


class Meta(SelfClosingTag):
    tag = u"meta"


class Hr(SelfClosingTag):
    tag = u"hr"


class OneLineTag(Element):

    def render(self, file_out, ind=u""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write(u"\n")
        file_out.write(ind)
        file_out.write(u"<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(u' %s="%s"'%(key, value) )
        file_out.write(u"> ")
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(unicode(child))
        file_out.write(u' </%s>'%self.tag)


class Title(OneLineTag):
    tag = u"title"


class A(OneLineTag):
    """
    element for a link ( <a> tag )
    """
    tag = u"a"
    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)


class Ul(Element):
    """
    element for an unordered list
    """
    tag = u"ul"


class Li(Element):
    """
    element for the item in a list
    """
    tag = u"li"


class H(OneLineTag):
    """
    class for header tags, the level is specified in a parameter

    """
    def __init__(self, level, content, **attributes):
        OneLineTag.__init__(self, content, **attributes)

        self.tag = u"h%i"%level


if __name__ == "__main__":
    import cStringIO
    page = Html()

    head = Head()
    head.append( Meta(charset="UTF-8") )
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(  H(2, "PythonClass - Class 6 example") )

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    list = Ul(id="TheList", style="line-height:200%")
    list.append( Li("The first item in a list") )
    list.append( Li("This is the second item", style="color: red") )
    item = Li()
    item.append("And this is a ")
    item.append( A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)

    page.append(body)


    f = cStringIO.StringIO()

    page.render(f)

    f.reset()
    print f.read()

    f.reset()
    open("test_html.html", 'w').write(f.read())

    print "new version"
