#!/usr/bin/env python
#
# util/create-iptypes-html.py v0.0.1
#
# Super hacky script to parse the input types CSV and output an HTML page that
# we can use as a user-facing reference.

import pandas as pd

# Read CSV
df = pd.read_csv('data/IPtypes.csv')

# Extract types using a list comprehension
ip_types = [ip_type for ip_type in df['Type']]

with open('docs/IPtypes.html', 'w', encoding="utf-8") as ip_types_html_f:
    ip_types_html_f.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="generator" content="HTML Tidy for HTML5 for Linux version 5.7.16">
  <meta charset="utf-8">
  <title>CG Core metadata schema</title>
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
  <div class="container-fluid">
    <div class="row">
      <main class="col">
        <h1>Information Products</h1>
        <p class="lead">This page provides the description of the information product types recommended by the CG Core metadata schema.</p>
        <p><a href="cgcore.html">Return to CG Core main page</a>.</p>
        <h2>Types of Information Product</h2>
''')

    # Write the row of buttons / badges
    for ip_type in ip_types:
        # Normalize types for use in identifiers, ie "Case Study" → "case-study"
        ip_type_short = ip_type.replace(' ', '-').lower()
        # No need writing new lines here since these are just badges
        ip_types_html_f.write(f"<a class='btn btn-sm btn-outline-primary m-1' href='#{ ip_type_short }'>{ ip_type }</a>")

    # Write a table for each type
    for ip_type in ip_types:
        ip_type_short = ip_type.replace(' ', '-').lower()
        ip_type_identifier = f'https://purl.org/cg/terms/{ ip_type_short }'

        # All items have definitions
        ip_type_description = df.query(f'Type == "{ ip_type }"')['Definition'].values.tolist()[0]

        # Begin writing table with common metadata
        ip_types_html_f.write(f'''<div class="col">
            <p class="invisible"><a id="{ ip_type_short }"></a></p>
            <table class="table table-sm table-bordered">
                <thead>
                    <tr class="table-secondary">
                    <th colspan="2">
                        { ip_type }
                        <div class="badge-class">
                            <span class="badge bg-primary align-middle">Class</span>
                        </div>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-2 field-name">Identifier</td>
                        <!-- 2023-09-25: identifiers should not be clickable yet, as many don't work -->
                        <td>{ ip_type_identifier }</td>
                    </tr>
                    <tr>
                        <td class="col-2 field-name">Definition</td>
                        <td>{ ip_type_description }</td>
                    </tr>''')

        # Get the synonymns, could be nan... this is a hack
        ip_type_synonyms = df.query(f'Type == "{ ip_type }"')['Synonyms'].values.tolist()[0]
        if isinstance(ip_type_synonyms, str):
            ip_types_html_f.write(f'''
                    <tr>
                        <td class="col-2 field-name">Synonyms</td>
                        <td>{ ip_type_synonyms }</td>
                    </tr>''')

        # Source
        ip_type_source = df.query(f'Type == "{ ip_type }"')['Source'].values.tolist()[0]
        if isinstance(ip_type_source, str):
            ip_types_html_f.write(f'''
                    <tr>
                        <td class="col-2 field-name">Source</td>
                        <td>{ ip_type_source }</td>
                    </tr>''')

        # Example link
        ip_type_example_link = df.query(f'Type == "{ ip_type }"')['Existing Outputs in Repositories'].values.tolist()[0]
        if isinstance(ip_type_example_link, str):
            ip_type_example_link = f'<a href="{ ip_type_example_link }">{ ip_type_example_link }</a>'
            ip_types_html_f.write(f'''
                    <tr>
                        <td class="col-2 field-name">Example</td>
                        <td>{ ip_type_example_link }</td>
                    </tr>''')

        # Specific guidance
        ip_type_guidance = df.query(f'Type == "{ ip_type }"')['Guidance'].values.tolist()[0]
        if isinstance(ip_type_guidance, str):
            ip_types_html_f.write(f'''
                    <tr>
                        <td class="col-2 field-name">Guidance</td>
                        <td>{ ip_type_guidance }</td>
                    </tr>''')

        # Wrap up the table for this type
        ip_types_html_f.write('''
                    </tbody>
                </table>
            </div>''')

    # Wrap up the page
    ip_types_html_f.write('''</main>
        </div>
      </div>
        <footer class="footer mt-auto">
          <div class="container">
            <p class="mb-0 py-1">CG Core Information Product Types.<span class="float-end"><a href="#">Back to top</a></span></p>
          </div>
        </footer>
      </body>
    </html>''')
