from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import time

from views import *
from models import *
from utils.utils import *
from . alertDialogController import Alerts, AlertType, IconType, AlertButton


class MyWebView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_WebView()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)


class MyApp(QMainWindow):
    countries = {
        "AF": "Afghanistan",
        "AX": "Aland Islands",
        "AL": "Albania",
        "DZ": "Algeria",
        "AS": "American Samoa",
        "AD": "Andorra",
        "AO": "Angola",
        "AI": "Anguilla",
        "AQ": "Antarctica",
        "AG": "Antigua and Barbuda",
        "AR": "Argentina",
        "AM": "Armenia",
        "AW": "Aruba",
        "AU": "Australia",
        "AT": "Austria",
        "AZ": "Azerbaijan",
        "BS": "Bahamas",
        "BH": "Bahrain",
        "BD": "Bangladesh",
        "BB": "Barbados",
        "BY": "Belarus",
        "BE": "Belgium",
        "BZ": "Belize",
        "BJ": "Benin",
        "BM": "Bermuda",
        "BT": "Bhutan",
        "BO": "Bolivia, Plurinational State of",
        "BQ": "Bonaire, Sint Eustatius and Saba",
        "BA": "Bosnia and Herzegovina",
        "BW": "Botswana",
        "BV": "Bouvet Island",
        "BR": "Brazil",
        "IO": "British Indian Ocean Territory",
        "BN": "Brunei Darussalam",
        "BG": "Bulgaria",
        "BF": "Burkina Faso",
        "BI": "Burundi",
        "KH": "Cambodia",
        "CM": "Cameroon",
        "CA": "Canada",
        "CV": "Cape Verde",
        "KY": "Cayman Islands",
        "CF": "Central African Republic",
        "TD": "Chad",
        "CL": "Chile",
        "CN": "China",
        "CX": "Christmas Island",
        "CC": "Cocos (Keeling) Islands",
        "CO": "Colombia",
        "KM": "Comoros",
        "CG": "Congo",
        "CD": "Congo, The Democratic Republic of the",
        "CK": "Cook Islands",
        "CR": "Costa Rica",
        "CI": "Côte d'Ivoire",
        "HR": "Croatia",
        "CU": "Cuba",
        "CW": "Curaçao",
        "CY": "Cyprus",
        "CZ": "Czech Republic",
        "DK": "Denmark",
        "DJ": "Djibouti",
        "DM": "Dominica",
        "DO": "Dominican Republic",
        "EC": "Ecuador",
        "EG": "Egypt",
        "SV": "El Salvador",
        "GQ": "Equatorial Guinea",
        "ER": "Eritrea",
        "EE": "Estonia",
        "ET": "Ethiopia",
        "FK": "Falkland Islands (Malvinas)",
        "FO": "Faroe Islands",
        "FJ": "Fiji",
        "FI": "Finland",
        "FR": "France",
        "GF": "French Guiana",
        "PF": "French Polynesia",
        "TF": "French Southern Territories",
        "GA": "Gabon",
        "GM": "Gambia",
        "GE": "Georgia",
        "DE": "Germany",
        "GH": "Ghana",
        "GI": "Gibraltar",
        "GR": "Greece",
        "GL": "Greenland",
        "GD": "Grenada",
        "GP": "Guadeloupe",
        "GU": "Guam",
        "GT": "Guatemala",
        "GG": "Guernsey",
        "GN": "Guinea",
        "GW": "Guinea-Bissau",
        "GY": "Guyana",
        "HT": "Haiti",
        "HM": "Heard Island and McDonald Islands",
        "VA": "Holy See (Vatican City State)",
        "HN": "Honduras",
        "HK": "Hong Kong",
        "HU": "Hungary",
        "IS": "Iceland",
        "IN": "India",
        "ID": "Indonesia",
        "IR": "Iran, Islamic Republic of",
        "IQ": "Iraq",
        "IE": "Ireland",
        "IM": "Isle of Man",
        "IL": "Israel",
        "IT": "Italy",
        "JM": "Jamaica",
        "JP": "Japan",
        "JE": "Jersey",
        "JO": "Jordan",
        "KZ": "Kazakhstan",
        "KE": "Kenya",
        "KI": "Kiribati",
        "KP": "Korea, Democratic People's Republic of",
        "KR": "Korea, Republic of",
        "KW": "Kuwait",
        "KG": "Kyrgyzstan",
        "LA": "Lao People's Democratic Republic",
        "LV": "Latvia",
        "LB": "Lebanon",
        "LS": "Lesotho",
        "LR": "Liberia",
        "LY": "Libya",
        "LI": "Liechtenstein",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "MO": "Macao",
        "MK": "Macedonia, Republic of",
        "MG": "Madagascar",
        "MW": "Malawi",
        "MY": "Malaysia",
        "MV": "Maldives",
        "ML": "Mali",
        "MT": "Malta",
        "MH": "Marshall Islands",
        "MQ": "Martinique",
        "MR": "Mauritania",
        "MU": "Mauritius",
        "YT": "Mayotte",
        "MX": "Mexico",
        "FM": "Micronesia, Federated States of",
        "MD": "Moldova, Republic of",
        "MC": "Monaco",
        "MN": "Mongolia",
        "ME": "Montenegro",
        "MS": "Montserrat",
        "MA": "Morocco",
        "MZ": "Mozambique",
        "MM": "Myanmar",
        "NA": "Namibia",
        "NR": "Nauru",
        "NP": "Nepal",
        "NL": "Netherlands",
        "NC": "New Caledonia",
        "NZ": "New Zealand",
        "NI": "Nicaragua",
        "NE": "Niger",
        "NG": "Nigeria",
        "NU": "Niue",
        "NF": "Norfolk Island",
        "MP": "Northern Mariana Islands",
        "NO": "Norway",
        "OM": "Oman",
        "PK": "Pakistan",
        "PW": "Palau",
        "PS": "Palestinian Territory, Occupied",
        "PA": "Panama",
        "PG": "Papua New Guinea",
        "PY": "Paraguay",
        "PE": "Peru",
        "PH": "Philippines",
        "PN": "Pitcairn",
        "PL": "Poland",
        "PT": "Portugal",
        "PR": "Puerto Rico",
        "QA": "Qatar",
        "RE": "Réunion",
        "RO": "Romania",
        "RU": "Russian Federation",
        "RW": "Rwanda",
        "BL": "Saint Barthélemy",
        "SH": "Saint Helena, Ascension and Tristan da Cunha",
        "KN": "Saint Kitts and Nevis",
        "LC": "Saint Lucia",
        "MF": "Saint Martin (French part)",
        "PM": "Saint Pierre and Miquelon",
        "VC": "Saint Vincent and the Grenadines",
        "WS": "Samoa",
        "SM": "San Marino",
        "ST": "Sao Tome and Principe",
        "SA": "Saudi Arabia",
        "SN": "Senegal",
        "RS": "Serbia",
        "SC": "Seychelles",
        "SL": "Sierra Leone",
        "SG": "Singapore",
        "SX": "Sint Maarten (Dutch part)",
        "SK": "Slovakia",
        "SI": "Slovenia",
        "SB": "Solomon Islands",
        "SO": "Somalia",
        "ZA": "South Africa",
        "GS": "South Georgia and the South Sandwich Islands",
        "ES": "Spain",
        "LK": "Sri Lanka",
        "SD": "Sudan",
        "SR": "Suriname",
        "SS": "South Sudan",
        "SJ": "Svalbard and Jan Mayen",
        "SZ": "Swaziland",
        "SE": "Sweden",
        "CH": "Switzerland",
        "SY": "Syrian Arab Republic",
        "TW": "Taiwan, Province of China",
        "TJ": "Tajikistan",
        "TZ": "Tanzania, United Republic of",
        "TH": "Thailand",
        "TL": "Timor-Leste",
        "TG": "Togo",
        "TK": "Tokelau",
        "TO": "Tonga",
        "TT": "Trinidad and Tobago",
        "TN": "Tunisia",
        "TR": "Turkey",
        "TM": "Turkmenistan",
        "TC": "Turks and Caicos Islands",
        "TV": "Tuvalu",
        "UG": "Uganda",
        "UA": "Ukraine",
        "AE": "United Arab Emirates",
        "GB": "United Kingdom",
        "US": "United States",
        "UM": "United States Minor Outlying Islands",
        "UY": "Uruguay",
        "UZ": "Uzbekistan",
        "VU": "Vanuatu",
        "VE": "Venezuela, Bolivarian Republic of",
        "VN": "Viet Nam",
        "VG": "Virgin Islands, British",
        "VI": "Virgin Islands, U.S.",
        "WF": "Wallis and Futuna",
        "YE": "Yemen",
        "ZM": "Zambia",
        "ZW": "Zimbabwe"
    }

    render_signal = pyqtSignal(list)

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LinkedinScraper()
        self.ui.setupUi(self)
        self.app = QApplication.instance()
        self.isAlive = False
        baseDir = os.path.dirname(__file__)
        self.ui.label_4.setPixmap(QtGui.QPixmap(os.path.join(baseDir,'..','assets','images','botintgram.png')))
        self.setWindowIcon(QIcon(os.path.join(baseDir,'..','assets','images','logo.png')))
        self.extra = {
            # Button colors
            'danger':  '#dc3545',
            'warning': '#ffc107',
            'success': '#1ff29a',
            # Font
            'font_family': 'Fira Code',
        }
        # css_utils.load_stylesheet(self.app,theme='light_purple.xml',extra=self.extra)
        css_utils.load_stylesheet(
            self.app, theme='dark_blue.xml', extra=self.extra)
        # self.ui.statusLbl.setProperty('class','statusLbl__connected')
        self.fillComboBox()
        self.setEvents()
        # self.ui.stackedWidget.setCurrentWidget(self.ui.resultPage)
        self.webview_interface = MyWebView()
        self.webview = self.webview_interface.ui.webview
        # self.webview_interface.show()
        self.webview.loadFinished.connect(self.on_load_finish)
        self.emails = []
        self.render_signal.connect(self.renderEmails)
        self.ui.backBtn.setEnabled(False)

    def setEvents(self):
        self.ui.startScraperBtn.clicked.connect(self.startScraperBtn_clicked)
        self.ui.stopBtn.clicked.connect(self.stopBtn_clicked)
        self.ui.backBtn.clicked.connect(self.backBtn_clicked)
        self.ui.exportBtn.clicked.connect(self.exportBtn_clicked)

    def stopBtn_clicked(self):
        self.isAlive = False
        self.ui.backBtn.setEnabled(True)

    def backBtn_clicked(self):
        self.ui.titleBodyLbl.setText('Craft Your Target')
        self.ui.stackedWidget.setCurrentWidget(self.ui.formPage)

    def exportBtn_clicked(self):
        if self.ui.emailsListWidget.count() == 0:
            Alerts.Show(AlertType.WARNING, 'Empty List.',
                        'Nothing to export. the list is empty!!!', IconType.WARNING, AlertButton.WARNING)
            return
        filename, _ = QFileDialog.getSaveFileName(
            None, "Save File", "list_items.txt", "Text Files (*.txt)")
        if filename:
            with open(filename, 'w') as file:
                for index in range(self.ui.emailsListWidget.count()):
                    item = self.ui.emailsListWidget.item(index)
                    file.write(item.text() + "\n")
            Alerts.Show(AlertType.SUCCESS, 'Done.', 'File Saved!',
                        IconType.SUCCESS, AlertButton.SUCCESS)

    def startScraperBtn_clicked(self):
        if self.ui.jobTitleLineEdit.text() == '':
            Alerts.Show(AlertType.WARNING, 'Empty Field',
                        'Please Enter job title!!!', IconType.WARNING, AlertButton.WARNING)
            return
        if self.ui.CountryComboBox.currentIndex() == -1:
            Alerts.Show(AlertType.WARNING, 'Empty Field',
                        'Please Select a country', IconType.WARNING, AlertButton.WARNING)
            return
        if self.ui.cityLineEdit.text() == '':
            Alerts.Show(AlertType.WARNING, 'Empty Field',
                        'Please Enter a city', IconType.WARNING, AlertButton.WARNING)
            return
        # print('Running...')
        self.ui.emailsListWidget.clear()
        self.isAlive = True
        self.ui.stopBtn.setEnabled(True)
        self.ui.backBtn.setEnabled(False)
        self.ui.label_8.setText('Running...')
        css_utils.set_class_attribute(
            self.ui.label_8, 'actionStatusLbl__running')
        self.emails = []
        self.ui.titleBodyLbl.setText('Fetching Emails...')
        self.ui.stackedWidget.setCurrentWidget(self.ui.resultPage)
        self.start()

    def fillComboBox(self):
        # for country in LinkedinScraper.countries:
        self.ui.CountryComboBox.addItems(LinkedinScraper.countries.values())

    def start(self):
        self.jobTitle = self.ui.jobTitleLineEdit.text()
        self.country = self.ui.CountryComboBox.currentText()
        self.city = self.ui.cityLineEdit.text()
        self.includes = self.ui.includeKeyLineEdit.text()
        self.excludes = self.ui.excludeKeyLineEdit.text()
        if self.build_query():
            self.webview.load(QUrl(self.urls.pop(0)))

    def scrapeResult(self, html):
        if self.isAlive:
            emails = self.extract_emails(html)
            self.render_signal.emit(emails)
            soup = BeautifulSoup(html, 'html.parser')
            pnnext = soup.select_one('#pnnext')
            recaptcha = soup.select_one('#recaptcha')
            if recaptcha:
                if not self.webview_interface.isVisible():
                    self.webview_interface.show()
            else:
                if self.webview_interface.isVisible():
                    self.webview_interface.hide()
                if pnnext:
                    self.webview.load(
                        QUrl('https://www.google.com' + pnnext.attrs['href']))
                else:
                    if len(self.urls) != 0:
                        self.webview.load(QUrl(self.urls.pop(0)))
                    else:
                        # print('************** Finish Scraping **************')
                        self.ui.stopBtn.setEnabled(False)
                        self.ui.backBtn.setEnabled(True)
                        self.ui.label_8.setText('Completed...')
                        css_utils.set_class_attribute(
                            self.ui.label_8, 'actionStatusLbl__completed')

    def renderEmails(self, emails):
        dummy = [
            '22@gmail.com',
            '22@hotmail.com',
            '22@live.com',
            '22@outlook.com',
            '22@yahoo.com',
            'x22@gmail.com',
            'x22@hotmail.com',
            'x22@live.com',
            'x22@outlook.com',
            'x22@yahoo.com'
        ]
        for email in emails:
            if email not in self.emails and email.lower() not in dummy:
                tmp = QListWidgetItem()
                tmp.setText(email)
                self.ui.emailsListWidget.addItem(tmp)
        self.ui.label_9.setText(f'Extracted : {self.ui.emailsListWidget.count()}')
        self.emails = list(set(self.emails + emails))

    def on_load_finish(self):
        # print('url load finished')
        self.webview.page().toHtml(lambda html: self.scrapeResult(html))

    def extract_emails(self, text):
        # Parse input text to remove HTML tags
        parsed_text = self.parse_text(text)

        # Find all unique email addresses within the parsed text
        email_regex = r'((\w+\.)?(\w+)\.?@\w*\.(com|net|org|(\w{2})))'
        matches = re.findall(email_regex, parsed_text,
                             flags=re.IGNORECASE | re.MULTILINE)
        unique_emails = list(set(matches))

        return list(set([email[0] for email in unique_emails]))

    def parse_text(self, text):
        # Replace HTML tags with empty strings
        tag_regex = r'<.*?>'
        return re.sub(tag_regex, '', text)

    def build_query(self):
        e = self.getCountryCode(self.country)
        if not e:
            self.urls = []
            return False
        self.urls = [
            f'https://www.google.com/search?q=site:{e}.linkedin.com "{self.jobTitle}" "{self.city}" "{self.includes}" intext:("@gmail.com" | "@hotmail.com" | "@live.com" | "@outlook.com" | "@yahoo.com") -inurl:"dir/" -intext:"{self.excludes}"',
            f'https://www.google.com/search?q=site:{e}.linkedin.com/pub "{self.jobTitle}" "{self.country}" "{self.includes}" intext:("@gmail.com" | "@hotmail.com" | "@live.com" | "@outlook.com" | "@yahoo.com") -inurl:"dir/" -intext:"{self.excludes}"',
            f'https://www.google.com/search?q=site:"www.linkedin.com" "{self.country}" "{self.jobTitle}" "{self.city}" "{self.includes}" intext:("@gmail.com" | "@hotmail.com" | "@live.com" | "@outlook.com" | "@yahoo.com") -inurl:"dir/" -intext:"{self.excludes}"',
            f'https://www.google.com/search?q=site:www.linkedin.com intext:"{self.country}" intext:"{self.jobTitle}" intext:("@gmail.com" | "@hotmail.com" | "@live.com" | "@outlook.com" | "@yahoo.com")'
        ]
        return True

    def closeEvent(self, event):
        self.webview_interface.close()
        super().closeEvent(event)

    def getCountryCode(self, country):
        for key, value in MyApp.countries.items():
            if value.lower() == country.lower():
                return key.lower()
        return None
