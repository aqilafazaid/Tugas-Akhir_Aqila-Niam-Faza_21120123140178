import tkinter as tk
from tkinter import ttk
import pandas as pd

# Create a list of dictionaries, each representing a Kanal Digital Wilayah Jawa Tengah-3 channel
channel_data = [
    {"channel_id": 1, "channel_name": "TVRI Jateng HD", "frekuensi": "30 UHF", "network": "Lembaga Penyiaran Publik TVRI", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
    {"channel_id": 2, "channel_name": "SCTV HD", "frekuensi": "33 UHF", "network": "EMTEK", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
    {"channel_id": 3, "channel_name": "TVONE HD", "frekuensi": "36 UHF", "network": "Lativi Media Karya", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
    {"channel_id": 4, "channel_name": "METRO TV HD", "frekuensi": "39 UHF", "network": "Media Group Network", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
    {"channel_id": 5, "channel_name": "RCTI HD", "frekuensi": "42 UHF", "network": "GTV Jateng-3", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
    {"channel_id": 6, "channel_name": "TRANSTV HD", "frekuensi": "45 UHF", "network": "TELEVISI TRANSFORMASI INDONESIA", "Lokasi pemancar": "Jatinegara, Kab. Tegal"},
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(channel_data)

class InformasiKanalDigitalWilayahJawaTengah3SystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Informasi Kanal Digital Wilayah Jawa Tengah 3")
        master.configure(bg="#EAEAEA")

        # Create style
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background="#EAEAEA", foreground="#333333", font=("Helvetica", 12))
        style.configure("TButton", background="#4CAF50", foreground="#FFFFFF", font=("Helvetica", 12, "bold"), relief="flat")
        style.configure("TFrame", background="#EAEAEA")
        style.configure("TRadiobutton", background="#EAEAEA", foreground="#333333", font=("Helvetica", 12))
        style.map("TButton", background=[("active", "#388E3C")])

        # Create notebook for tabbed interface
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create frames for the notebook tabs
        self.search_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.search_tab, text="Search Channels")
        self.notebook.add(self.history_tab, text="Search History")

        # Search tab UI elements
        self.create_search_tab()

        # History tab UI elements
        self.create_history_tab()

        # Initialize search history list
        self.search_history = []

    def create_search_tab(self):
        # Header frame
        self.header_frame = ttk.Frame(self.search_tab)
        self.header_frame.pack(fill=tk.X, padx=20, pady=10)

        # Search frame
        self.search_frame = ttk.Frame(self.search_tab)
        self.search_frame.pack(fill=tk.X, padx=20, pady=10)

        # Results frame
        self.results_frame = ttk.Frame(self.search_tab)
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Header label
        self.header_label = ttk.Label(self.header_frame, text="Informasi Kanal Digital Wilayah Jawa Tengah 3", font=("Comic Sans MS", 25, "bold"))
        self.header_label.pack(pady=10)

        # Search label
        self.search_label = ttk.Label(self.search_frame, text="Search by:", font=("Times New Roman", 17))
        self.search_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.search_type_var = tk.StringVar()
        self.search_type_var.set("channel_name")  # Set default search type

        self.search_type_radiobutton1 = ttk.Radiobutton(
            self.search_frame, text="Channel Name", variable=self.search_type_var, value="channel_name"
        )
        self.search_type_radiobutton1.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.search_type_radiobutton2 = ttk.Radiobutton(
            self.search_frame, text="Network", variable=self.search_type_var, value="network"
        )
        self.search_type_radiobutton2.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.search_entry = ttk.Entry(self.search_frame, width=40, font=("Helvetica", 12))
        self.search_entry.grid(row=3, column=0, sticky=tk.W, pady=5)

        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_channels, style="TButton")
        self.search_button.grid(row=4, column=0, pady=10)

        # Add additional buttons
        self.show_all_button = ttk.Button(self.search_frame, text="Show All Channels", command=self.show_all_channels, style="TButton")
        self.show_all_button.grid(row=4, column=1, padx=10)

        self.clear_button = ttk.Button(self.search_frame, text="Clear Results", command=self.clear_results, style="TButton")
        self.clear_button.grid(row=4, column=2, padx=10)

        # Add a scrollbar for the results frame
        self.canvas = tk.Canvas(self.results_frame, bg="#EAEAEA")
        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def create_history_tab(self):
        self.history_label = ttk.Label(self.history_tab, text="Search History", font=("Comic Sans MS", 25, "bold"))
        self.history_label.pack(pady=10)

        self.history_listbox = tk.Listbox(self.history_tab, font=("Helvetica", 12))
        self.history_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def search_channels(self):
        search_term = self.search_entry.get().strip().lower()
        search_type = self.search_type_var.get()

        if search_term:
            filtered_df = df[df[search_type].str.lower().str.contains(search_term)]
        else:
            filtered_df = df

        self.display_results(filtered_df)
        self.add_to_history(search_term, search_type)

    def show_all_channels(self):
        self.display_results(df)

    def clear_results(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def display_results(self, results_df):
        # Clear previous results
        self.clear_results()

        # Display new results
        if results_df.empty:
            result_label = ttk.Label(self.scrollable_frame, text="No results found.", font=("Helvetica", 12), background="#FFFFFF", relief="solid", padding=10)
            result_label.pack(fill=tk.X, pady=2)
        else:
            for index, row in results_df.iterrows():
                result_text = (f"Channel ID: {row['channel_id']} \nChannel Name: {row['channel_name']} \nFrekuensi: {row['frekuensi']} \nNetwork: {row['network']} \n"
                               f"Lokasi Pemancar: {row['Lokasi pemancar']}")
                result_label = ttk.Label(self.scrollable_frame, text=result_text, background="#FFFFFF", relief="solid", anchor="center", padding=10, font=("Helvetica", 12))
                result_label.pack(fill=tk.X, pady=2, padx=20)

    def add_to_history(self, search_term, search_type):
        if search_term:
            history_entry = f"{search_type.replace('_', ' ').title()}: {search_term}"
            self.search_history.append(history_entry)
            self.update_history_listbox()

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for entry in self.search_history:
            self.history_listbox.insert(tk.END, entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = InformasiKanalDigitalWilayahJawaTengah3SystemGUI(root)
    root.mainloop()

