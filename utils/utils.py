import os
from qt_material import apply_stylesheet
import cssutils
import sys


class css_utils:
    app_stylesheet = ''
    app_stylesheet_dict = {}
    
    @staticmethod
    def load_colors_variables():
        tab = [
            'primaryColor',
            'primaryLightColor',
            'secondaryColor',
            'secondaryLightColor',
            'secondaryDarkColor',
            'primaryTextColor',
            'secondaryTextColor',
            'danger',
            'warning',
            'success',
            'info',
        ]
        app_custom_colors = {
            'danger': '#dc3545',
            'warning':'#ffc107',
            'success':'#1ff29a',
            'info': '#17a2b8'
        }
        style_path = os.path.join(os.path.dirname(__file__),'..','assets','css','style.qss')
        with open(style_path,'r') as file:
            lines = file.readlines()
            content = ''.join(lines[13:]) # dont get variables because it dont work in pyqt!!!
        for color in tab:
            if os.environ.get(color):
                content = content.replace(f'var(--{color})',os.environ.get(color))
            else:
                content = content.replace(f'var(--{color})',app_custom_colors[color])
        css_utils.app_stylesheet = content
        css_utils.generate_dict_stylesheet()
        return content
        
    @staticmethod
    def load_stylesheet(app,theme,extra,style_path='style.qss'):
        '''
        Load a theme and set some custom stylesheet
        '''
        apply_stylesheet(app, theme=theme,extra=extra)
        style_path = os.path.join(os.path.dirname(__file__),'..','assets','css',style_path)
        custom_style = css_utils.load_colors_variables()
        app.setStyleSheet(app.styleSheet() + custom_style)
    
    @staticmethod
    def generate_dict_stylesheet():
        parsed_stylesheet = cssutils.parseString(css_utils.app_stylesheet)
        for rule in parsed_stylesheet:
            selector = rule.selectorText
            styles = rule.style.cssText
            css_utils.app_stylesheet_dict[selector] = styles
        
        
    
    @staticmethod
    def set_class_attribute(widget,class_name):
        '''
        Add a css class to a widget
        '''
        widget.setProperty('class',class_name)
        widget.setStyleSheet(css_utils.app_stylesheet_dict[f'.{class_name}'])
    
    # @staticmethod
    # def setFonts(self):
    #     self.font_id = QFontDatabase.addApplicationFont(os.path.join(baseDir,'assets','Roboto.ttf'))
    #     font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
    #     self.setStyleSheet(f"\nfont-family: '{font_family}';\n" + self.styleSheet())
    #     font = QFont(font_family)
    #     font.setPointSize(12)
    #     self.ui.comboBox.setFont(font)
    

class helpers:
    @staticmethod
    def get_chrome_profile_path():
        if sys.platform == 'win32':
            chrome_profile_path = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default')
        elif sys.platform == 'darwin':
            chrome_profile_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default')
        elif sys.platform.startswith('linux'):
            chrome_profile_path = os.path.expanduser('~/.config/google-chrome/Default')
        else:
            raise Exception("Your platform is not supported")

        if not os.path.isdir(chrome_profile_path):
            raise Exception("Chrome profile not found")
        return chrome_profile_path