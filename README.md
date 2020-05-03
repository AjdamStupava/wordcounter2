# wordcounter2
Tento program spočíta znaky, slová a riadky zo vstupného textového súboru.
Na spustenie programu je nutné zadať vstupný súbor.
Ak chcem, aby spočítal iba jednu alebo niektoré z položiek, treba to napísať s dvomi spojovníkmi za vstupný súbor. (vstup.txt --znaky -- slova)
Program využíva užívateľský vstup argparse.
Znaky sa počítajú ako celková dĺžka reťazca, do ktorého sa načíta text z textového súboru.
//Slová vo vstupnom súbore musia byť oddelené iba medzerami, prípadne enterom na konci riadka. Nesmú byť medzi nimi dve medzery alebo prázdny riadok, inak počet slov vrátený nebude správny. Na univerzálnom algoritme na počítanie slov sa pracuje a bude implementovaný do programu.// Univerzálny algorimtus na počítanie slov bol dokončený a implementovaný, vstupný textový súbor môže obsahovať hocijaké znaky a chyby, slová budú spočítané správne.
Riadky sa počítajú na základe počtu znakov pre koniec riadka (\n).
