"""
Client + internal deck for Espoo: price-structure evolution.

Built from Espoo_ Hintarakenteen kehitys (1).docx — covers cost drivers,
Google Cloud changes, security landscape, bot traffic, and workload overrun.

Narrative: evidence base for adjusting service pricing after five years of
shifting operating conditions.

Run:   python -m examples.espoo_hintarakenne
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.mearra_deck import MearraDeck


def build() -> Path:
    deck = MearraDeck()

    # ---- Cover ---------------------------------------------------------
    deck.add_cover(
        title="Hintarakenteen kehitys",
        subtitle="Espoon kaupungin verkkopalvelu",
        presenter_line="Mearra · Sopimuskauden katsaus 2026",
        variant="indigo",
    )

    # ---- Section 1: Johdanto ------------------------------------------
    deck.add_section_header(
        title="Johdanto",
        eyebrow="Tässä dokumentissa",
    )

    deck.add_title_body(
        title="Miksi hintarakennetta on tarve tarkastella?",
        body=(
            "Tässä dokumentissa perehdytään Espoon kaupungin verkkopalvelun "
            "tuottamiseen liittyvien kustannusten kehitykseen sekä "
            "toimintaympäristön muutoksiin sopimuskauden aikana.\n\n"
            "Viimeisen viiden vuoden aikana palveluntuotannon lähtökohdat ovat "
            "muuttuneet merkittävästi: hintaindeksi on noussut, pilvi­resurssien "
            "markkina on muuttunut, tietoturva­vaatimukset ovat kasvaneet ja "
            "bottiliikenne vaatii jatkuvaa aktiivista hallintaa."
        ),
        eyebrow="Yhteenveto",
    )

    # ---- Section 2: Kustannusten kehitys -------------------------------
    deck.add_section_header(
        title="Kustannusten kehitys",
        eyebrow="Hintarakenne",
    )

    # Producer price index
    deck.add_big_number(
        number="8,3 %",
        label="hintaindeksin nousu sopimuskaudella",
        context=(
            "Palvelujen tuottajahintaindeksi on noussut 8,3 % sopimuskauden aikana. "
            "Tämä heijastuu suoraan palveluntuotannon kustannuksiin."
        ),
        eyebrow="Palvelujen tuottajahintaindeksi",
    )

    # CDN + WAF domain issue
    deck.add_title_body(
        title="CDN- ja WAF-hinnoittelu perustuu domain-määrään",
        body=(
            "Mearran CDN- ja WAF-palveluiden hinnoittelu perustuu olettamaan "
            "kohtuullisesta määrästä hallittavia domaineja.\n\n"
            "Espoon kaupungin domain-määrä on poikkeuksellisen korkea — "
            "lähes 70 kpl. Jokainen näistä muodostaa toimittajalla erillisen "
            "kustannuserän, mikä kumuloituu kuukausittaisiin laskuihin."
        ),
        eyebrow="CDN + WAF",
    )

    # Hosting cost breakdown table
    deck.add_table(
        title="Hosting-kustannusten erittely",
        eyebrow="Kustannustaso 3/26",
        headers=["Kulu / palvelu", "Kustannus"],
        rows=[
            ["CDN Expenses 3/26", "125,75 €"],
            ["WAF Expenses 3/26", "412,63 €"],
            ["Capacity expenses (Compute)", "~30 €"],
            ["Filestore", "63 €"],
            ["CDN services (68 kpl)", "136 €"],
            ["Instana", "~120 €"],
            ["Sumologic", "~120 €"],
            ["Muut pienemmät palvelut", "~100 €"],
            ["Yhteensä", "1 011,38 €"],
        ],
        col_widths=[6.40, 2.50],
    )

    # Small services grouped
    deck.add_three_columns(
        title="Muut pienemmät palvelut",
        eyebrow="Kokonaiskuva",
        columns=[
            {
                "title": "VALVONTA & LOKIT",
                "body": (
                    "Uptimerobot\n"
                    "Splunk\n"
                    "Pingdom\n"
                    "Uptime.com\n"
                    "Sumologic"
                ),
                "icon": "accessibility",
            },
            {
                "title": "VIESTINTÄ & YHTEYDET",
                "body": (
                    "Sparkpost\n"
                    "Telia M"
                ),
                "icon": "cloud",
            },
            {
                "title": "KEHITYS & CI",
                "body": (
                    "GitHub\n"
                    "CircleCI"
                ),
                "icon": "ai",
            },
        ],
    )

    # ---- Section 3: Google Cloud -muutokset ----------------------------
    deck.add_section_header(
        title="Googlen muutokset",
        eyebrow="Pilvi­resurssien markkina on muuttunut",
    )

    deck.add_title_body(
        title="Spot-nodeista on pitänyt luopua pääosin",
        body=(
            "Google Cloudin (GCP) Spot-nodejen luotettavuuden heikkeneminen ja "
            "lisääntynyt epävakaus ovat johtaneet rakenteelliseen muutokseen siinä, "
            "miten palveluita tarjotaan.\n\n"
            "Taustalla on kolme tekijää, jotka ovat muuttaneet pilvi­resurssien "
            "markkinaa. Verkkopalvelut, joilta vaaditaan jatkuvaa saatavuutta, eivät "
            "enää kestä Spot-nodejen korkeaa poistuma-astetta — tästä seuraa siirtymä "
            "kalliimpiin, varattuihin (on-demand) instansseihin."
        ),
        eyebrow="Rakenteellinen muutos",
    )

    # Three reasons
    deck.add_three_columns(
        title="Kolme syytä Spot-nodejen epävakauteen",
        eyebrow="Markkinamuutos",
        columns=[
            {
                "title": "AI-BUUMIN RESURSSIPULA",
                "body": (
                    "Tekoälymallien räjähdysmäinen kasvu on varannut valtavan "
                    "määrän fyysistä palvelinkapasiteettia. Google ottaa "
                    "Spot-resursseja takaisin omaan käyttöönsä, mikä nostaa "
                    "palveluntarjoajien kustannuksia."
                ),
                "icon": "ai",
            },
            {
                "title": "DYNAAMINEN SYKLI",
                "body": (
                    "Vanhat Spot-nodet sammuivat ennakoitavasti viimeistään "
                    "24 tunnin kohdalla. Nykyiset voidaan keskeyttää milloin "
                    "tahansa kysynnän noustessa — tämä tekee niistä "
                    "arvaamattomia."
                ),
                "icon": "cloud",
            },
            {
                "title": "BIN-PACKING OPTIMOINTI",
                "body": (
                    "Google täyttää konesalinsa entistä tiiviimmin. "
                    "\"Löysää\" kapasiteettia on vähemmän ja automaatio reagoi "
                    "sekunneissa, mikä aiheuttaa Spot-nodejen välittömiä "
                    "uudelleen­käynnistyksiä."
                ),
                "icon": "accessibility",
            },
        ],
    )

    deck.add_title_body(
        title="Kustannusvaikutus: siirtymä vakaisiin instansseihin",
        body=(
            "Verkkopalvelut, jotka vaativat jatkuvaa saatavuutta tai joiden "
            "palautuminen uudelleen­käynnistyksestä on hidasta, eivät enää kestä "
            "Spot-nodejen nykyistä poistuma-astetta.\n\n"
            "Tämä on pakottanut siirtymään kalliimpiin mutta vakaisiin varattuihin "
            "(on-demand) instansseihin — merkittävä kustannus­vaikutus, joka ei ole "
            "palveluntuottajan valittavissa."
        ),
        eyebrow="Yhteenveto",
    )

    # ---- Section 4: Tietoturvallisuus ----------------------------------
    deck.add_section_header(
        title="Tietoturvallisuusvaatimusten kasvu",
        eyebrow="Muuttunut uhka­ympäristö",
    )

    deck.add_title_subtitle_body(
        title="Venäjän valtion tukema toiminta",
        subtitle="Uhkaprofiili muuttui Suomen NATO-jäsenyyden jälkeen.",
        body=(
            "Uhkaprofiili on siirtynyt \"opportunistisista lunnasohjelmistoista\" "
            "\"jatkuvaan valtion tukemaan häirintään\". Espoo.fi:n kaltaiset palvelut "
            "kohtaavat nyt jatkuvia DDoS-hyökkäyksiä poliittisten virstanpylväiden "
            "aikana sekä kehittyneitä \"hitaasti ja vähitellen\" tapahtuvia "
            "vakoilu­yrityksiä, joiden tavoitteena on kerätä tietoja kansalaisista tai "
            "infrastruktuurista.\n\n"
            "Tämä on merkittävästi kasvattanut palveluiden tarjoamiseen vaadittavia "
            "tietoturva­vaatimuksia. Hyvänä esimerkkinä toimii Mearran JA3-pohjainen "
            "DDoS-suojaus, jolla on suojattu Espoota useamman kerran."
        ),
        eyebrow="Valtiolliset toimijat",
    )

    deck.add_title_subtitle_body(
        title="Toimitusketjuhyökkäysten raju kasvu",
        subtitle="Kansainvälisesti pahimmaksi tunnistettu tietoturvauhka.",
        body=(
            "Hyökkääjät eivät enää yritä murtautua sisään perinteisin tavoin — "
            "he murtautuvat toimitusketjun kautta, eli niiden komponenttien kautta, "
            "joista verkkopalvelut rakentuvat. Painopiste on siirtynyt ohjelmiston "
            "osaluetteloihin (SBOM).\n\n"
            "Jokainen kolmannen osapuolen laajennus, JavaScript-kirjasto ja API on "
            "auditoitava, jotta \"myrkytetty\" päivitys ei vaaranna tietoja. "
            "Tyypillisessä verkkopalvelussa tällaisia komponentteja on satoja tai "
            "tuhansia, mikä on tuonut merkittävän määrän uusia vastuita."
        ),
        eyebrow="Toimitusketju hyökkäysvektorina",
    )

    deck.add_title_body(
        title="AI-avusteiset hyökkäykset",
        body=(
            "Viimeisen viiden vuoden aikana tekoäly on muuttanut kyberhyökkäykset "
            "teollisen mittakaavan operaatioiksi — pelkkä määrän kasvu ei ole ainoa "
            "haaste, vaan hyökkäysten nopeus ja mukautuvuus ovat nousseet kriittisiksi.\n\n"
            "Vuoteen 2026 tultaessa hyökkääjät hyödyntävät autonomisia "
            "\"agenttimalleja\", jotka suorittavat tiedustelua, murtavat suojauksia ja "
            "muuttavat taktiikkaansa reaaliajassa ilman ihmisen ohjausta. Keskimääräinen "
            "murtoaika on lyhentynyt kymmeniin minuutteihin. Tämä vaatii siirtymistä "
            "staattisista säännöistä ennakoivaan uhka­havainnointiin ja automatisoituun "
            "vastatoimintaan."
        ),
        eyebrow="Tekoäly uhkakuvassa",
    )

    # ---- Section 5: Bottiliikenne --------------------------------------
    deck.add_section_header(
        title="Verkkoliikenne ja bottisuojaus",
        eyebrow="Espoo.fi-palvelussa",
    )

    deck.add_title_body(
        title="Bottiliikenne vaatii aktiivista hallintaa",
        body=(
            "Verkkopalveluihin kohdistuva bottiliikenne on kasvanut maailman­laajuisesti. "
            "Espoo.fi-palvelun liikenteestä keskimäärin 3 % on bottien aiheuttamaa, "
            "mutta ajoittaiset piikit voivat nostaa määrää merkittävästi — tämä "
            "aiheuttaa ylimääräisiä infra­struktuuri­kustannuksia ja kuormittaa "
            "järjestelmiä.\n\n"
            "Turvataksemme palvelun laadun ja kustannus­tehokkuuden olemme ottaneet "
            "käyttöön dynaamisen luokittelun: hyödylliset botit päästetään sivustolle "
            "esteettä, haitalliset tunnistetaan ja eliminoidaan aktiivisesti."
        ),
        eyebrow="3 % keskimääräistä liikennettä on botteja",
    )

    deck.add_two_columns(
        title="Dynaaminen luokittelu käytössä",
        eyebrow="Hyödyllinen vs. haitallinen",
        left_title="HYÖDYLLISET BOTIT",
        left_body=(
            "Varmistamme, että esimerkiksi hakukoneiden botit pääsevät sivustolle "
            "esteettä. Tämä on kriittistä Espoo.fi:n paikallisen näkyvyyden "
            "(GEO- ja SEO-näkyvyys) ja löydettävyyden kannalta."
        ),
        right_title="HAITALLISET BOTIT",
        right_body=(
            "Tunnistamme ja eliminoimme aktiivisesti pahantahtoisen liikenteen — "
            "palvelun­estohyökkäykset (DDoS) ja muut haitalliset automaatiot — "
            "ennen kuin ne vaikuttavat loppukäyttäjän kokemukseen."
        ),
        left_icon="accessibility",
        right_icon="ai",
    )

    # ---- Section 6: Työmääräkuorma -------------------------------------
    deck.add_section_header(
        title="Ylläpitokuorma",
        eyebrow="Budjetoitu vs. toteutunut",
    )

    deck.add_big_number(
        number="5x",
        label="budjetoitu työmäärä huippukuukausina",
        context=(
            "Espoon ylläpitokuorma on moninkertainen budjetoituun nähden. "
            "Joinakin kuukausina kiinteään hintaan budjetoitu työmäärä "
            "ylittyy lähes viisinkertaisesti — lähes 500 % budjetoidusta."
        ),
        eyebrow="Työmääräkuorma",
    )

    # ---- Closing summary ----------------------------------------------
    deck.add_title_body(
        title="Yhteenveto: hintarakenteen tarkastelu",
        body=(
            "Sopimuskauden aikana palveluntuotannon lähtökohdat ovat muuttuneet "
            "usealla rintamalla samanaikaisesti:\n\n"
            "Hintaindeksi on noussut 8,3 %. Domain-määrä on poikkeuksellinen ja "
            "kumuloituu laskuihin. Google Cloudin muutokset ovat pakottaneet siirtymään "
            "kalliimpiin instansseihin. Tietoturva­vaatimukset ovat kasvaneet "
            "merkittävästi Venäjän toiminnan, toimitusketju­hyökkäysten ja "
            "AI-avusteisten hyökkäysten myötä. Ylläpitokuorma ylittää budjetoidun "
            "huippu­kuukausina lähes viisinkertaisesti.\n\n"
            "Nämä muutokset edellyttävät palvelun hinnoittelun tarkastelua, jotta "
            "palvelun laatu ja turvallisuus voidaan pitää nykyisellä tasolla."
        ),
        eyebrow="Seuraavat askeleet",
    )

    deck.add_thank_you(subtitle="mearra.com")

    out = _resolve_output_path("espoo-hintarakenne.pptx")
    deck.save(out)
    return out


def _resolve_output_path(filename: str) -> Path:
    """Find the active Cowork session's outputs folder, or fall back to cwd."""
    import os
    override = os.environ.get("COWORK_OUTPUTS")
    if override:
        base = Path(override)
    else:
        candidates = sorted(Path("/sessions").glob("*/mnt/outputs"))
        base = candidates[0] if candidates else Path.cwd()
    base.mkdir(parents=True, exist_ok=True)
    return base / filename


if __name__ == "__main__":
    path = build()
    print(f"Wrote {path}")
