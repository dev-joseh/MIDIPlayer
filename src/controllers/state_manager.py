
class StateManager:
    """
    - Gerencia os estados e transições do app e sinaliza a interface para atualização
    - EXEMPLO: Tocando, pausado, parado
    """
    def __init__(self):
        # Estado inicial do app
        self.current_state = "stopped"
        self.observers = []  # Lista de funções que precisam ser notificadas quando o estado mudar

    def add_observer(self, observer_func):
        """Adiciona uma função que será chamada quando o estado mudar."""
        self.observers.append(observer_func)

    def _notify_observers(self):
        """Notifica todas as funções cadastradas sobre o estado atual."""
        for observer in self.observers:
            observer(self.current_state)

    def set_state(self, new_state):
        """Define um novo estado e notifica os observadores."""
        if new_state != self.current_state:
            self.current_state = new_state
            print(f"Estado alterado para: {self.current_state}")
            self._notify_observers()

    def is_playing(self):
        return self.current_state == "playing"

    def is_paused(self):
        return self.current_state == "paused"

    def is_stopped(self):
        return self.current_state == "stopped"
