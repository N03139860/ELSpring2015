#!/usr/bin/env python

#original code https://github.com/Pyplate/rpi_temp_logger/blob/master/webgui.py

import cgi
import cgitb
import getData


# global variables
dbname='/../../local.db'


# print the HTTP header
def printHTTPheader():
    print   """
            <!DOCTYPE html>\n\n
           
            """


# print the HTML head section
# arguments are the page title and the table for the chart
def printHTMLHead(title, table):
    print "<head>"
    print "    <title>"
    print title
    print "    </title>"
    print """
        <!-- Latest compiled and minified CSS -->\n
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n

        <!-- Optional theme -->\n
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n
        """
    
    print_graph_script(table)

    print "</head>"


# convert rows from database into a javascript table
def create_table(rows):
    chart_table=""

    for row in rows[:-1]:
        rowstr="['{0}', {1}],\n".format(str(row[0][:-4]),str(row[1]))
        chart_table+=rowstr

    row=rows[-1]
    rowstr="['{0}', {1}]\n".format(str(row[0][:-4]),str(row[1]))
    chart_table+=rowstr

    return chart_table

# print the javascript to generate the chart
# pass the table generated from the database info
def print_graph_script(table):

    # google chart snippet
    chart_code="""
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Time', 'Temperature'],
%s
        ]);
        var options = {
            title: 'Temperature',
            curveType: 'function',
            vAxis:{"title":"Temperature(Celsius)"},
            hAxis:{"title":"Date and Time"},
            legend:"none"
        };
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>"""

    print chart_code % (table)




# print the div that contains the graph
def show_graph():
    
    print '<div id="chart_div" style="width: 100%; height: 500px;"></div>'




def print_time_form():

    print """
        <div class='row'>
        <div class='pull-right'>
        <div class="form-inline">
        <div class="form-group">
        <form action="/cgi-bin/get-temperature/getTemperature.py" method="GET">
        <label for="time">Time (int) </label> 
        <input type="text" name="timeinterval" class="form-control" placeholder="Insert the interval">
        </form>
        </div>
        <button type="submit" value="Go Get It" class="btn btn-success">Go Get It!</button>
        </div>
        </div>
        </div>
        """

# check that the option is valid
# and not an SQL injection
def validate_input(input_str):
    # check that the option string represents a number
    if input_str.isalnum():
        # check that the option is within a specific range
        if int(input_str) > 0 and int(input_str) <= 500:
            return input_str
        else:
            return None
    else: 
        return None


#return the option passed to the script
def get_input():
    form=cgi.FieldStorage()
    if "timeinterval" in form:
        input_str = form["timeinterval"].value
        return validate_input (input_str)
    else:
        return None




# main function
# This is where the program starts 
def main():

    cgitb.enable()

    # get options that may have been passed to this script
    input_str=get_input()

    if input_str is None:
        input_str = "120"

    # get data from the database
    records=getData.get_data('../../local.db',int(input_str))

    # print the HTTP header
    printHTTPheader()

    if len(records) != 0:
        # convert the data into a table
        table=create_table(records)
    else:
        print "No data found"
        return

    # start printing the page
    print """
        <html lang="en">\n\n
        
        """
    # print the head section including the table
    # used by the javascript for the chart
    printHTMLHead("Raspberry Pi Temperature Logger", table)

    # print the page body
    print "<body>"
   
    print ""
    print """
            <nav class="navbar navbar-inverse navbar-fixed-top">
              <div class="container">
                <div class="navbar-header">
                  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                  </button>
                  <a class="navbar-brand" href="#">Raspberry Pi Temperature Logger - Frederico Castro</a>
                </div>
              </div>
            </nav>
    """
    print """
            <div class='container'>
            """
    print "<hr>"
    
    print """ 
    <hr>
    <div class='row'>
    <h2 style='margin-top:20px;'>Temperature Chart</h2>
    </div>
    <hr>
    """
    print_time_form()
    show_graph()
    print """
            </div>"""
    print "</body>"
    print "</html>"


if __name__=="__main__":
    main()
