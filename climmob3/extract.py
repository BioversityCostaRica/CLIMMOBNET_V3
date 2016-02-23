from jinja2.ext import babel_extract as extract_jinja2
import jinja_extensions as je

jinja_extensions = '''
                    jinja2.ext.do, jinja2.ext.with_,
                    climmob3.jinja_extensions.SnippetExtension
                   '''

# This function take badly formatted html with strings etc and make it beautiful
# generally remove surlus whitespace and kill \n this will break <code><pre>
# tags but they should not be being translated '''
def jinja2_cleaner(fileobj, *args, **kw):

    # Take badly formatted html with strings etc before goes to the translation .pot file

    # This code is based on CKAN code which is licensed as follows
    #
    # CKAN - Data Catalogue Software
    # Copyright (C) 2007 Open Knowledge Foundation
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as
    # published by the Free Software Foundation, either version 3 of the
    # License, or (at your option) any later version.
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU Affero General Public License for more details.
    # You should have received a copy of the GNU Affero General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>.

    kw['options']['extensions'] = jinja_extensions

    raw_extract = extract_jinja2(fileobj, *args, **kw)

    for lineno, func, message, finder in raw_extract:

        if isinstance(message, basestring):
            message = je.regularise_html(message)
        elif message is not None:
            message = (je.regularise_html(message[0])
                       ,je.regularise_html(message[1]))

        yield lineno, func, message, finder

# This custom extractor is to support customs tags in the babel jinja2 extractions. Otherwise the normal extract fail
def extract_climmob3(fileobj, *args, **kw):

    # This code is based on CKAN code which is licensed as follows
    #
    # CKAN - Data Catalogue Software
    # Copyright (C) 2007 Open Knowledge Foundation
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as
    # published by the Free Software Foundation, either version 3 of the
    # License, or (at your option) any later version.
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU Affero General Public License for more details.
    # You should have received a copy of the GNU Affero General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>.

    fileobj.read()
    output = jinja2_cleaner(fileobj, *args, **kw)
    fileobj.seek(0)
    return output