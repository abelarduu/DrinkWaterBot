from plyer import notification
from colorama import init, Fore, Style
from pyfiglet import Figlet
import time

class App:
    def __init__(self):
        """Inicializa as variáveis principais do programa."""
        self.title = '💧 Hora de se Hidratar!'
        self.message = 'Opa! Que tal tomar um copo d’água agora para manter seu corpo saudável? 🥤'
        self.app_name = 'DrinkWaterBot'
        self.app_icon = 'assets/icon.ico'
        self.start_time = self.get_current_time('%H:%M:%S')
        self.start_minutes = self.get_current_time('%M:%S')
        self.has_notified = False
        
        # Inicializa o colorama para garantir que funcione corretamente no Windows
        init(autoreset=True)
        
    def get_current_time(self, time_format) -> str:
        """Obtém o horário atual no formato especificado."""
        return time.strftime(time_format, time.localtime())
        
    def display_banner(self):
        """Exibe o Titulo do app no terminal com tipografia detalhada e colorida."""
        figlet_font = Figlet(font='standard')
        txt_icon = figlet_font.renderText(self.app_name)
        app_banner = f"{Fore.LIGHTBLUE_EX}{txt_icon}{Style.RESET_ALL}"

        print(app_banner)
        
    def display_message(self):
        """Exibe notificações do app no terminal com tipografia colorida."""
        # Exibição no terminal a notificação com horário e título coloridos
        print(f"\n{Fore.LIGHTBLUE_EX}{self.get_current_time('%H:%M:%S')} {self.title}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}{self.get_current_time('%H:%M:%S')}{Style.RESET_ALL} - {self.message}")
        
    def notify(self):
        """Exibe uma notificação para lembrar de beber água.""" 
        notification.notify(title=self.title,
                            message=self.message,
                            app_name=self.app_name,
                            app_icon=self.app_icon)
        
        # Exibição no terminal
        self.display_message()

        
    def main_loop(self):
        """Executa o loop principal para checar e exibir notificações."""
        while True:
            if self.get_current_time('%H:%M:%S') == self.start_time:
                self.display_banner()
                self.notify()
            
            else:
                self.message = 'Já passou uma hora! Que tal tomar um copo d’água agora para manter seu corpo saudável? 🥤'
                current_time = self.get_current_time('%M:%S')
                self.has_notified = False
            
                if (not self.has_notified and current_time == self.start_minutes):
                    self.notify()
                    self.has_notified = True
            
            # Delay de 1 segundo
            time.sleep(1)
                
if __name__ == "__main__":
    app = App()
    app.main_loop()
