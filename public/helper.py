from bs4 import BeautifulSoup

html_code = """
<!-- The provided HTML table code -->
<table>
<tbody>
<tr>
<th class="bg-blue-400 text-white p-4"><strong>Sr.No</strong></th>
<th class="bg-blue-400 text-white p-4"><strong>Month</strong></th>
<th class="bg-blue-400 text-white p-4"><strong>Year</strong></th>
<th class="bg-blue-400 text-white p-4"><strong>Training Conducted Information </strong></th>
</tr>
<tr >
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> 1</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> AUG</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> 2015</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> Two day National Workshop on "LaTeX for Technical Documentation" from Aug 21-Aug 22, 2015</td>
</tr>
<tr >
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> 2</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> JULY</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> 2014</td>
<td class="bg-white border-b-4 border-gray-200 text-black p-4"> Short-term Course on Pattern Analysis and Information Security (PAIS), 30 June - 4 July, 2014</td>
</tr>
</tbody>
</table> 


"""
# <th class="bg-blue-400 text-white p-4">
# <td class="bg-white border-b-4 border-gray-200 text-black p-4"> 
# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Remove all style and span tags
for tag in soup.find_all(['style', 'span']):
    tag.decompose()

# Get the modified HTML code
modified_html = str(soup)
print(modified_html)
