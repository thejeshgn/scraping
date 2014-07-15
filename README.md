# My Scraping Bootstrap  #

Scrapes "Data" and saves into SQLITE. Can also export into CSV, JSON and DBF



## Use ##
Fork the project and use it


## Install Dependencies ##
`
pip install -r requirements
`

## To run ##

`
python scrape.py
`


### Export data as json and csv ####
`
#you will have to edit export.yaml for the correct tables which you want to export
datafreeze export.yaml
`

### Export data as dbf ####
`
#depends on csv files created above so first created them
#you will have to edit export_dbf.py for the correct csv and column names
python export_dbf.py
`



## Author ##

Thejesh GN <i@thejeshgn.com>

Fingerprint: C7D4 1911 9893 ADAF 27B0 FCAA BFFC 8DD3 C06D D6B0

<table>
  <tr>
    <td><img src="http://www.gravatar.com/avatar/4545b2a84b0ae407abc97ad8f23cc28b?s=60"></td><td valign="middle">Thejesh GN<br><a href="http:/thejeshgn.com">http://thejeshgn.com</a></td>
    <td>i-at-thejeshgn-com <br> GPG ID :  0xBFFC8DD3C06DD6B0</td>
  </tr>
</table>


## License ##
Data Scraper IMD data scrapes reservoir data and saves into SQLITE. Can also export into CSV, JSON, DBF
 
Copyright (C) 2014  Thejesh GN <i@thejeshgn.com>

### Data
Data is under ODC Open Database License (ODbL)

### Code
Data is under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
