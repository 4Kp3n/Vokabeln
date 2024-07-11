---
created: 2024-05-03T15:00
updated: 2024-07-03T07:20
---
TARGET DECK: Modul3

START
Einfach
Vorderseite:
### Erkläre die Stride-Methode

Rückseite:
Ein Framework zur Identifizierung und Analyse von Sicherheitsbedrohungen. 
STRIDE steht für die sechs Bedrohungskategorien 
- Spoofing, 
- Tampering, 
- Repudiation 
- Information Disclosure 
- Denial of Service 
- Elevation of Privilege

END

START
Einfach
Vorderseite:
### Was ist Spoofing

Rückseite:
### Vortäuschen der Identität einer anderen Person, eines anderen Geräts, System oder Service

betroffenes Schutzziel => Authentizität

END
START
Einfach
Vorderseite:
### Was ist Tampering

Rückseite:
### Manipulation von Informationen oder Daten in einer Datenbank

betroffenes Schutzziel => Integrität

END
START
Einfach
Vorderseite:
### Erkläre den Begriff Repudiation

Rückseite:
### Leugnen oder Bestreiten einer Handlung oder Transaktion

betroffenes Schutzziel => Nicht-Abstreitbarkeit

END
START
Einfach
Vorderseite:
### Was ist Information Disclosure 

Rückseite:
### unbefugte Offenlegung vertraulicher / sensibler Informationen

betroffenes Schutzziel => Vertraulichkeit

END
START
Einfach
Vorderseite:
### Was ist Denial of Service 

Rückseite:

### Funktionalität des Systems / Geräts / Service so blockieren, dass eine normale Nutzung nicht mehr möglich ist

betroffenes Schutzziel => Verfügbarkeit

Sonderform DDOS: Überflutung einer Website oder eines Service durch Anfragen von sehr vielen Unterschiedlichen Absendern, zB von einem Botnetz, so dass zusätzlich Schutzmechanismen ausgehebelt werden. 

END

START
Einfach
Vorderseite:
### Erkläre Elevation of Privilege

Rückseite:
deutsch: Erweiterung von Privilegien
### Ausweitung der Rechte eines Users

betroffene Schutzziele => abhängig von der neuen Berechtigung

 eine Taktik, die eingesetzt wird, um unberechtigt höhere Berechtigungen in einem Zielsystem zu erlangen

END

START
Einfach
Vorderseite:
### Was ist ein APT

Rückseite:
### Advanced Pesistant Threat

Advanced: Fortschrittlich, technisch raffiniert, nutzt hochentwickelte Techniken / Technologien oder Zero-Day-Exploits

Persistant: Der Angriff ist darauf ausgelegt, über einen langen Zeitraum unentdeckt zu bleiben, um kontinuierlich Daten zu sammeln oder weitere Systeme zu infiltrieren.

Treat: Gezielter Angriff gegen spezifische Ziele wie KRITIS-Unternehmen, Konzerne oder Regierungsbehörden

Cyberangriff, der durch seine hohe Raffinesse und Langfristigkeit gekennzeichnet ist. APTs sind komplex, gut organisiert und oft von staatlichen Akteuren oder hochspezialisierten Cyberkriminellen ausgeführt. 

END

START
Einfach
Vorderseite:
### Erkläre CVE

Rückseite:
### **Common Vulnerabilities and Exposures**. 

Eine Liste von öffentlich bekannten Sicherheitslücken in Software- und Hardwareprodukten. 

Jede Sicherheitslücke erhält eine eindeutige Kennung, die sogenannte CVE-ID, um sie eindeutig identifizieren und darüber berichten zu können.

END

START
Einfach
Vorderseite:
### Nenne die Phasen der Bedrohungsmodellierung

Rückseite:

- Designphase, das System wird in einem Diagramm dargestellt
- Problemfindung, Analyse des Systems zB mittels STRIDE
- Behebung, Behandlung der Bedrohung nach Priorisierung
- Überprüfung, ob die Bedrohung erfolgreich eliminiert / mitigiert wurde
![[Bedrohungsmodellierung.png]]


END

START
Einfach
Vorderseite:
### Nenne 5 Elemente zur Erstellung eines Datenflussdiagramms

Rückseite:
- Prozess
- Datenspeicher
- Externe Entität
- Datenfluss
- Vertrauensgrenze

END

START
Einfach
Vorderseite:
### In welche zwei grundsätzlichen Kategorien kann ich die **Umsetzung** (Do! des PDCA - Zyklus) des BCMS unterteilen?

(Erkläre die beiden Kategorien anhand der Darstellung auf der Rückseite in eigenen Worten)

Rückseite:

Der Prozessschritt Aufbau und Befähigung der BAO beinhaltet alle Aspekte, um eine funktionierende BAO zu etablieren, die im Not- und Krisenfall sofort erreichbar und ar￾beitsfähig ist.
Alle weiteren Prozessschritte in der DO-Phase dienen der angemessenen Absicherung der zeitkritischen Geschäftsprozesse. 
Fast jeder dieser Schritte verbessert die Mög￾lichkeiten, einen Vorfall in einer geordneten BC-Planung zu behandeln anstatt nur reak￾tiv in einer Krise.

![[BCMS_Kategorien.png]]

![[BCMS_Legende.png]]

END


START
Einfach
Vorderseite:
### Beschreibe die Stufen eines BCMS 

Rückseite:

- BCM: "Geschäftsfortführungs-Management-System" 
- Ziel: Geschäftsprozesse gegen Ausfälle absichern
- + Ausfallzeitverringerung bei Krisen/Notfällen
- Einstieg/Reihenfolge beim Aufbau nicht relevant
Reaktiv-BCMS -> Aufbau-BCMS -> Standard-BCMS 
![[BCMS_Stufenmodell.png]]

END

START
Einfach
Vorderseite:
### Was versteht man unter Kerberoasting?
 
Rückseite:
- Ein Angriff auf das Kerberos Protokoll. 
- Ein authentifizierter AD Benutzer (Vorraussetzung) fordert Service Tickets der Service Accounts an und versucht anschließend die enthaltenen Password-Hashes offline zu knacken.

END