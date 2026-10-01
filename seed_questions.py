import os
import sys

# Ensure UPSC_Agile directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from extensions import db
from models import QuizQuestion

questions_data = [
    # ── POLITY & GOVERNANCE ──
    {
        "topic": "Polity",
        "question": "With reference to the 'Doctrine of Basic Structure' in the Indian Constitution, consider the following statements:\n1. It was first explicitly defined in Article 368 by the 42nd Constitutional Amendment Act, 1976.\n2. The Supreme Court of India in Kesavananda Bharati case (1973) held that the Parliament's constituent power does not enable it to alter the basic structure.\n3. The concept of Judicial Review itself forms part of the basic structure.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "B",
        "explanation": "Statement 1 is incorrect: The Constitution does not define 'Basic Structure'; it is a judicial doctrine evolved by the Supreme Court in Kesavananda Bharati (1973). Statement 2 is correct: Parliament cannot alter the basic structure under Art 368. Statement 3 is correct: Judicial review was affirmed as part of basic structure in Indira Nehru Gandhi (1975) and Minerva Mills (1980)."
    },
    {
        "topic": "Polity",
        "question": "Consider the following statements regarding the Ordinance-making power of the President under Article 123:\n1. An Ordinance can be issued only when both Houses of Parliament are not in session.\n2. The President's satisfaction to promulgate an Ordinance is justiciable on grounds of mala fide.\n3. An Ordinance cannot be promulgated to amend the Constitution of India.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "B",
        "explanation": "Statement 1 is incorrect: An ordinance can be promulgated when either of the two Houses is not in session (or both). Statement 2 is correct: In Cooper (1970) & DC Wadhwa (1987), President's satisfaction was held to be justiciable. Statement 3 is correct: An ordinance cannot amend the Constitution."
    },
    {
        "topic": "Polity",
        "question": "Regarding the Writ jurisdiction in India, which of the following statements is INCORRECT?",
        "option_a": "The Supreme Court cannot issue writs for any purpose other than the enforcement of Fundamental Rights.",
        "option_b": "The High Court can issue writs against any person, authority and government not only within its territorial jurisdiction but also outside if the cause of action arises within.",
        "option_c": "The writ of Quo-Warranto can be sought only by an aggrieved person and not by any interested citizen.",
        "option_d": "The writ of Prohibition is available only against judicial and quasi-judicial authorities.",
        "correct_option": "C",
        "explanation": "Option C is incorrect (hence the answer): Quo-Warranto can be sought by any interested person, not necessarily by an aggrieved party (exception to locus standi)."
    },
    {
        "topic": "Polity",
        "question": "With reference to the Money Bill in the Indian Parliament, consider the following statements:\n1. If any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the Lok Sabha thereon is final.\n2. The Rajya Sabha has no power to amend or reject a Money Bill; it can only make recommendations within 14 days.\n3. The President can return a Money Bill for reconsideration of the Parliament.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statement 3 is incorrect: Under Article 111, the President may give assent or withhold assent to a Money Bill, but cannot return it for reconsideration because it is introduced with the President's prior recommendation."
    },
    {
        "topic": "Polity",
        "question": "Which of the following Constitutional provisions directly empower the Union Government to issue directions to the States?\n1. Article 256 (Compliance of State laws with Union laws)\n2. Article 257 (Control of the Union over States in certain cases like construction of means of communication)\n3. Article 365 (Effect of failure to comply with, or to give effect to, directions given by the Union)\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "D",
        "explanation": "All three statements are correct: Under Art 256 and 257, the Union can give executive directions to States. Art 365 states that failure to comply with Union directions may invite President's rule under Art 356."
    },
    {
        "topic": "Polity",
        "question": "With reference to the Finance Commission of India, consider the following:\n1. It is a quasi-judicial body constituted by the President under Article 280 every 5th year or earlier.\n2. The recommendations made by the Finance Commission are legally binding on the Union Government.\n3. The Chairman must be a retired Supreme Court or High Court judge.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "1 and 2 only",
        "option_c": "2 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statement 1 is correct: Constituted under Article 280. Statement 2 is incorrect: Recommendations are advisory in nature, not legally binding. Statement 3 is incorrect: Chairman must be a person having experience in public affairs (Act of 1951)."
    },
    {
        "topic": "Polity",
        "question": "Consider the following statements regarding Anti-Defection Law (Tenth Schedule):\n1. It does not apply to a nominated member if they join a political party within six months of taking their seat.\n2. An independent member becomes disqualified if they join any political party after election.\n3. The law originally permitted split in a party by one-third members, which was omitted by the 91st Constitutional Amendment Act, 2003.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1, 2 and 3",
        "option_d": "1 and 3 only",
        "correct_option": "C",
        "explanation": "All three statements are correct: 1) Nominated members can join within 6 months without defection; 2) Independent members are disqualified if they join ANY party; 3) 91st Amendment removed the 1/3 split defense, retaining only 2/3 merger defense."
    },

    # ── ECONOMY ──
    {
        "topic": "Economy",
        "question": "With reference to 'Open Market Operations' (OMOs) conducted by the Reserve Bank of India, what is its primary objective?",
        "option_a": "To regulate long-term external commercial borrowings of corporations",
        "option_b": "To adjust rupee liquidity conditions in the market on a durable basis",
        "option_c": "To fix foreign exchange rates against special drawing rights (SDR)",
        "option_d": "To finance the fiscal deficit directly through monetisation",
        "correct_option": "B",
        "explanation": "OMOs involve outright purchase and sale of government securities in open market by RBI to regulate durable liquidity conditions in the banking system."
    },
    {
        "topic": "Economy",
        "question": "In the context of the Indian Economy, which of the following will lead to an INCREASE in the Money Multiplier?",
        "option_a": "Increase in the Cash Reserve Ratio (CRR)",
        "option_b": "Increase in the Statutory Liquidity Ratio (SLR)",
        "option_c": "Increase in the banking habit of the population",
        "option_d": "Increase in the currency deposit ratio by public",
        "correct_option": "C",
        "explanation": "Money Multiplier = 1 / Reserve Ratio (broadly). When banking habits improve, people deposit more cash with banks (currency deposit ratio decreases), allowing banks to create more credit and raising the money multiplier."
    },
    {
        "topic": "Economy",
        "question": "Consider the following statements regarding 'Inverted Duty Structure':\n1. It refers to a situation where the import duty on finished goods is higher than the import duty on raw materials and intermediate inputs.\n2. It discourages domestic value addition and manufacturing competitiveness.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "2 only",
        "option_c": "Both 1 and 2",
        "option_d": "Neither 1 nor 2",
        "correct_option": "B",
        "explanation": "Statement 1 is incorrect: Inverted Duty Structure occurs when import duties on raw materials/inputs are HIGHER than on finished goods. Statement 2 is correct: This disadvantages domestic manufacturers compared to foreign finished imports."
    },
    {
        "topic": "Economy",
        "question": "Which of the following items are included in the calculation of Gross National Product (GNP) at Market Prices?\n1. Remittances received from Indian citizens working abroad\n2. Income generated by foreign companies in India\n3. Subsidies granted by the government\nSelect the correct answer using the code given below:",
        "option_a": "1 only",
        "option_b": "1 and 3 only",
        "option_c": "2 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "GNP = GDP + Net Factor Income from Abroad (NFIA). Remittances by Indians abroad are factor income from abroad, so they are added. Income generated by foreign entities in India is subtracted. Subsidies are subtracted when calculating at Market Prices (GDP_MP = GDP_FC + Net Indirect Taxes, where NIT = Indirect Taxes - Subsidies)."
    },
    {
        "topic": "Economy",
        "question": "With reference to 'Core Inflation' in macroeconomic terminology, it differs from Headline Inflation because it excludes:",
        "option_a": "Capital goods and infrastructure sectors",
        "option_b": "Food and fuel articles subject to volatile price movements",
        "option_c": "Services sector and digital commerce",
        "option_d": "Exports and imports of crude petroleum",
        "correct_option": "B",
        "explanation": "Core Inflation strips out the volatile components—specifically food and energy/fuel items—to reveal the underlying persistent trend of general inflation."
    },
    {
        "topic": "Economy",
        "question": "What happens when a central bank raises the 'Policy Repo Rate'?\n1. Cost of borrowing for commercial banks increases.\n2. Aggregate demand in the economy generally tends to contract.\n3. Domestic currency generally tends to appreciate in foreign exchange markets.\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "D",
        "explanation": "When Repo rate is hiked: borrowing costs rise, lowering credit expansion and dampening aggregate demand (curbing inflation). Higher yields also attract foreign capital, appreciating the domestic currency."
    },
    {
        "topic": "Economy",
        "question": "Consider the following statements regarding the 'Current Account Deficit' (CAD) of India:\n1. A high CAD is always financed solely through the drawdown of foreign exchange reserves.\n2. Services export surplus typically helps moderate India's merchandise trade deficit.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "2 only",
        "option_c": "Both 1 and 2",
        "option_d": "Neither 1 nor 2",
        "correct_option": "B",
        "explanation": "Statement 1 is incorrect: CAD is routinely financed by surplus in the Capital Account (FDI, FPI, External Commercial Borrowings) without needing reserve drawdown unless capital inflows are insufficient. Statement 2 is correct: India's massive software and business services exports generate invisibles surplus."
    },

    # ── ENVIRONMENT & ECOLOGY ──
    {
        "topic": "Environment",
        "question": "Which of the following protected areas in India is famous for being the only floating national park in the world, home to the endangered Sangai deer?",
        "option_a": "Keibul Lamjao National Park",
        "option_b": "Bhitarkanika National Park",
        "option_c": "Namdapha National Park",
        "option_d": "Khangchendzonga National Park",
        "correct_option": "A",
        "explanation": "Keibul Lamjao National Park in Manipur is located on Loktak Lake, characterized by floating decomposed plant matter known as 'Phumdis', and is the sole habitat of the Brow-antlered deer (Rucervus eldii eldii) or Sangai."
    },
    {
        "topic": "Environment",
        "question": "With reference to 'Bio-magnification' and 'Bio-accumulation', consider the following statements:\n1. Bio-accumulation refers to an increase in concentration of a pollutant across successive trophic levels of a food chain.\n2. Bio-magnification occurs when an organism absorbs a toxic substance at a rate greater than that at which the substance is lost.\n3. Pollutants that bio-magnify are typically fat-soluble and non-biodegradable.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "3 only",
        "option_c": "2 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "B",
        "explanation": "Statements 1 and 2 are swapped: Bio-accumulation happens within a single organism/trophic level over time. Bio-magnification happens across successive trophic levels. Statement 3 is correct: lipophilic (fat-soluble) and persistent compounds (like DDT, Mercury) magnify."
    },
    {
        "topic": "Environment",
        "question": "Which of the following International Conventions and Protocols is correctly paired with its subject matter?\n1. Basel Convention : Transboundary movements of hazardous wastes\n2. Rotterdam Convention : Prior Informed Consent for certain hazardous chemicals in international trade\n3. Minamata Convention : Phase-out of ozone-depleting substances\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Pair 3 is incorrect: Minamata Convention deals with Mercury pollution. Ozone-depleting substances are governed by the Vienna Convention and Montreal Protocol."
    },
    {
        "topic": "Environment",
        "question": "With reference to 'Blue Carbon', which of the following coastal and marine ecosystems are significant sinks for it?\n1. Mangrove forests\n2. Tidal marshes\n3. Seagrass meadows\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "D",
        "explanation": "Blue carbon is carbon captured by world's coastal and ocean ecosystems. Mangroves, tidal salt marshes, and seagrass meadows sequester carbon at rates significantly faster than terrestrial tropical forests."
    },
    {
        "topic": "Environment",
        "question": "In the context of wildlife conservation in India, consider the following statements regarding the Wildlife (Protection) Act, 1972:\n1. It prohibits the hunting of all wild animals specified in Schedule I to IV except under certain licensed conditions.\n2. Vermin animals are listed in a separate schedule and can be hunted without license.\n3. The Wildlife (Protection) Amendment Act, 2022 reduced the total number of schedules to four.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "1 and 3 only",
        "option_c": "2 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "B",
        "explanation": "Statement 2 is outdated/incorrect: The 2022 Amendment completely removed Schedule V (vermin), so vermin cannot be hunted unchecked unless specifically notified by the Centre under Sec 62. Statements 1 and 3 are correct."
    },
    {
        "topic": "Environment",
        "question": "Which of the following factors are primary triggers for the phenomenon known as 'Eutrophication' in aquatic water bodies?\n1. Influx of synthetic nitrogen and phosphorus agricultural fertilizers\n2. Discharge of untreated sewage into lakes\n3. Increase in dissolved oxygen saturation\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Eutrophication is caused by nutrient enrichment (Nitrogen & Phosphorus) leading to algal blooms. This subsequently causes hypoxia (sharp decrease in dissolved oxygen), not an increase."
    },
    {
        "topic": "Environment",
        "question": "Consider the following statements regarding Biosphere Reserves in India:\n1. The core zone of a Biosphere Reserve allows non-destructive research and sustainable tourism.\n2. The Nilgiri Biosphere Reserve was the first Biosphere Reserve in India included under UNESCO's MAB program.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "2 only",
        "option_c": "Both 1 and 2",
        "option_d": "Neither 1 nor 2",
        "correct_option": "B",
        "explanation": "Statement 1 is incorrect: The core zone is strictly legally protected from all human interference except non-destructive research and monitoring. Tourism is restricted to the buffer zone and transition area. Statement 2 is correct: Nilgiri was designated in 1986 and included in UNESCO MAB in 2000."
    },

    # ── HISTORY & ART & CULTURE ──
    {
        "topic": "History",
        "question": "With reference to the Indus Valley Civilization, consider the following statements:\n1. Chanhudaro was exclusively devoted to craft production including bead-making and seal-making.\n2. Dholavira is renowned for its unique tripartite city layout and massive water reservoir system.\n3. Domestic architecture at Harappa reveals that windows opened directly onto main thoroughfares for cross-ventilation.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan houses had an inward-looking courtyard layout; main entrance and windows opened into quiet side alleys, not onto main thoroughfares, maintaining privacy and dust protection."
    },
    {
        "topic": "History",
        "question": "Regarding the administration under the Mauryan Empire as described in Kautilya's Arthashastra, match the following officials with their duties:\n1. Samaharta : Chief collector of revenue\n2. Sannidhata : Chief custodian of the state treasury\n3. Sitadhyaksha : Superintendent of royal crown agriculture lands\nSelect the correct code:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1, 2 and 3",
        "option_d": "1 and 3 only",
        "correct_option": "C",
        "explanation": "All three pairs are accurate according to Arthashastra: Samaharta handled assessment and collection; Sannidhata maintained storehouses and treasury; Sitadhyaksha supervised state agricultural lands (Sita)."
    },
    {
        "topic": "History",
        "question": "Consider the following statements regarding the Bhakti movement in medieval India:\n1. Ramanuja propounded the philosophy of Vishishtadvaita (qualified non-dualism).\n2. Madhvacharya advocated Shuddhadvaita (pure non-dualism).\n3. Shankaracharya established the philosophy of Advaita (monism).\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "1 and 3 only",
        "option_c": "2 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "B",
        "explanation": "Statement 2 is incorrect: Madhvacharya propounded Dvaita (dualism). Shuddhadvaita was formulated by Vallabhacharya. Statements 1 and 3 are correct."
    },
    {
        "topic": "History",
        "question": "With reference to the Vijayanagara Empire, consider the following statements:\n1. The Hazara Rama temple was built for the exclusive private worship of the royal family.\n2. The Amara-Nayaka system was a major political innovation where military commanders were assigned territories called Amaram.\n3. Domingo Paes and Fernao Nuniz were Portuguese travelers who visited the Vijayanagara court.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1, 2 and 3",
        "option_d": "1 and 3 only",
        "correct_option": "C",
        "explanation": "All three statements are correct: Hazara Rama temple is located in royal center; Amara-nayakas were military chiefs who retained contingents and sent annual tribute; Paes visited during Krishnadeva Raya and Nuniz during Achyuta Deva Raya."
    },
    {
        "topic": "History",
        "question": "In the context of the Indian Freedom Struggle, the 'August Offer' of 1940 proposed which of the following?\n1. Dominion status as the objective for India\n2. Expansion of the Viceroy's Executive Council with a majority of Indians\n3. Immediate transfer of defense and foreign affairs to an Indian provisional government\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect: The British refused any immediate transfer of defense, external affairs, or minority interests during the war; it only promised a constituent assembly post-war."
    },
    {
        "topic": "History",
        "question": "Who among the following was the founder of the 'Satya Shodhak Samaj' (1873), aimed at liberating lower castes from the exploitation of orthodox traditions?",
        "option_a": "Jyotirao Phule",
        "option_b": "B. R. Ambedkar",
        "option_c": "Gopal Hari Deshmukh (Lokahitawadi)",
        "option_d": "E. V. Ramasamy Periyar",
        "correct_option": "A",
        "explanation": "Jyotirao Phule founded Satya Shodhak Samaj in Pune in 1873 to emphasize education, emancipation of Dalits and women, and wrote Gulamgiri."
    },
    {
        "topic": "Art & Culture",
        "question": "Consider the following pairs of Indian Classical Dance forms and their characteristic features:\n1. Kathakali : Marked by elaborate face makeup (chutti) and dramatized facial expressions with mudras.\n2. Sattriya : Evolved in the monasteries (Satras) of Assam by Srimanta Sankardev.\n3. Mohiniyattam : Known as the dance of the enchantress, performed exclusively with heavy acrobatic leaps.\nWhich of the pairs given above is/are correctly matched?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Pair 3 is incorrect: Mohiniyattam is characterized by graceful, swaying, delicate body movements and gentle footwork resembling the breeze through palm leaves, devoid of abrupt or acrobatic leaps."
    },

    # ── GEOGRAPHY ──
    {
        "topic": "Geography",
        "question": "Consider the following statements regarding the 'Coriolis Force':\n1. It is directly proportional to the angle of latitude, being zero at the Equator and maximum at the Poles.\n2. It acts perpendicular to the pressure gradient force.\n3. It causes moving winds and ocean currents to deflect to the left in the Northern Hemisphere.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statement 3 is incorrect: Ferrel's Law states that Coriolis force deflects moving objects to the RIGHT in the Northern Hemisphere and to the LEFT in the Southern Hemisphere. Statements 1 and 2 are correct."
    },
    {
        "topic": "Geography",
        "question": "Which of the following rivers is/are right-bank tributaries of the River Ganga?\n1. Yamuna\n2. Son\n3. Gomati\n4. Punpun\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "1, 2 and 4 only",
        "option_c": "2, 3 and 4 only",
        "option_d": "1, 3 and 4 only",
        "correct_option": "B",
        "explanation": "Yamuna, Son, and Punpun join Ganga from its southern/right bank. Gomati originates in Pilibhit and joins Ganga from the left (northern) bank."
    },
    {
        "topic": "Geography",
        "question": "With reference to the 'Western Disturbances' that bring winter rain to northwestern India, consider the following statements:\n1. They originate as extra-tropical cyclones over the Mediterranean Sea.\n2. They are steered towards the Indian subcontinent by the Subtropical Westerly Jet Stream.\n3. They are highly beneficial for the Kharif crops in Punjab and Haryana.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statement 3 is incorrect: Western disturbances occur in winter (Dec-Feb) and provide vital rainfall for RABI crops (especially wheat), not Kharif crops."
    },
    {
        "topic": "Geography",
        "question": "Regarding volcanic landforms, match the intrusive igneous body with its description:\n1. Batholith : Large granitic bodies formed at deep depths of crust\n2. Laccolith : Dome-shaped intrusive body connected by a pipe-like conduit from below\n3. Sill : Horizontal sheet of solidified magma between sedimentary strata\nWhich of the above pairs are correctly matched?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1, 2 and 3",
        "option_d": "1 and 3 only",
        "correct_option": "C",
        "explanation": "All three pairs are correct geological definitions of intrusive volcanic features."
    },
    {
        "topic": "Geography",
        "question": "Consider the following statements regarding 'Thermal Inversion' in the atmosphere:\n1. It occurs when a layer of warm air lies over a layer of cold air near the Earth's surface.\n2. Long winter nights, clear skies, and calm air promote ground-level temperature inversion.\n3. In hilly terrains, inversion causes cold air to drain into valley bottoms, causing frost damage to orchards.\nWhich of the statements given above are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "D",
        "explanation": "All three statements are correct: Under normal conditions, temperature decreases with altitude. Inversion inverts this gradient; cold air drainage (katabatic winds) in valleys frequently leads to severe localized valley frosts."
    },
    {
        "topic": "Geography",
        "question": "Which of the following straits connects the Red Sea with the Gulf of Aden, serving as a strategic maritime chokepoint?",
        "option_a": "Strait of Hormuz",
        "option_b": "Bab-el-Mandeb Strait",
        "option_c": "Strait of Malacca",
        "option_d": "Bosporus Strait",
        "correct_option": "B",
        "explanation": "Bab-el-Mandeb (Gate of Tears) connects the Red Sea to Gulf of Aden/Arabian Sea. Strait of Hormuz connects Persian Gulf to Gulf of Oman."
    },

    # ── SCIENCE & TECHNOLOGY ──
    {
        "topic": "Science & Tech",
        "question": "With reference to 'CRISPR-Cas9' genetic scissors, which won the Nobel Prize in Chemistry in 2020, consider the following:\n1. Cas9 is an enzyme that acts as molecular scissors to cut DNA at a specified site.\n2. The guide RNA (gRNA) directs the Cas9 protein to the exact matching target sequence.\n3. It can be used to edit genes only in animal cells, but not in plants or microbes.\nWhich of the statements given above is/are correct?",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "Statement 3 is incorrect: CRISPR-Cas9 is universally applicable across organisms, including plants, bacteria, fungi, animals, and human cells."
    },
    {
        "topic": "Science & Tech",
        "question": "In the context of space technology, what is the significance of the 'Lagrange Point L1' where India's Aditya-L1 solar mission is placed?",
        "option_a": "It is a point where the gravitational pull of Earth and Sun equals zero.",
        "option_b": "It is a gravitational equilibrium point allowing continuous uninterrupted view of the Sun without any occultation or eclipses.",
        "option_c": "It is located in low-Earth polar orbit for high-resolution magnetosphere imaging.",
        "option_d": "It allows a spacecraft to stay stationary relative to Mars and Jupiter.",
        "correct_option": "B",
        "explanation": "Lagrange Point 1 (L1) provides a major advantage of observing the Sun without any occultation/eclipses, allowing real-time solar activity and space weather monitoring."
    },
    {
        "topic": "Science & Tech",
        "question": "With reference to 'Quantum Key Distribution' (QKD), consider the following statements:\n1. It utilizes principles of quantum mechanics like superposition and entanglement to securely share encryption keys.\n2. Any eavesdropping attempt fundamentally alters the quantum state of photons and alerts the communicators.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "2 only",
        "option_c": "Both 1 and 2",
        "option_d": "Neither 1 nor 2",
        "correct_option": "C",
        "explanation": "Both statements are correct. In QKD, keys are transmitted via qubits (photons). Under Heisenberg's uncertainty principle and the no-cloning theorem, any measurement by an intruder collapses the quantum state, revealing the eavesdropping instantly."
    },
    {
        "topic": "Science & Tech",
        "question": "What is the primary difference between mRNA vaccines and conventional attenuated viral vaccines?",
        "option_a": "mRNA vaccines inject a weakened live pathogen, whereas conventional vaccines deliver artificial RNA strands.",
        "option_b": "mRNA vaccines teach cells how to make a harmless viral protein that triggers an immune response without using any live or dead virus.",
        "option_c": "mRNA vaccines alter the host organism's permanent genomic DNA inside the cell nucleus.",
        "option_d": "Conventional vaccines trigger only humoral immunity while mRNA vaccines trigger neither humoral nor cellular immunity.",
        "correct_option": "B",
        "explanation": "mRNA vaccines instruct host ribosomes in cytoplasm to produce a harmless spike protein, prompting the immune system to generate antibodies. They never enter the nucleus and do not alter genomic DNA."
    },
    {
        "topic": "Science & Tech",
        "question": "Consider the following statements regarding 'Solid State Batteries' compared to traditional Lithium-ion batteries:\n1. They use a solid electrolyte instead of liquid or gel polymer electrolytes.\n2. They possess higher energy density and drastically lower fire/explosion risks.\nWhich of the statements given above is/are correct?",
        "option_a": "1 only",
        "option_b": "2 only",
        "option_c": "Both 1 and 2",
        "option_d": "Neither 1 nor 2",
        "correct_option": "C",
        "explanation": "Both statements are correct: Solid-state batteries replace volatile flammable liquid electrolytes with solid ceramics, glasses, or polymers, boosting energy density and safety."
    },
    {
        "topic": "Science & Tech",
        "question": "Which of the following optical phenomena is solely responsible for the propagation of light signals through fiber optic cables?",
        "option_a": "Diffraction of light",
        "option_b": "Total Internal Reflection",
        "option_c": "Polarization of electromagnetic waves",
        "option_d": "Rayleigh scattering",
        "correct_option": "B",
        "explanation": "Optical fibers rely on Total Internal Reflection (TIR) occurring when light travels from a denser core to a rarer cladding at an angle exceeding the critical angle."
    },
    {
        "topic": "Polity",
        "question": "Under the Constitution of India, which of the following categories of Bills require the prior recommendation of the President before introduction in Parliament?\n1. A Bill altering the boundaries of any State (Article 3)\n2. A Money Bill (Article 117(1))\n3. A Constitutional Amendment Bill (Article 368)\nSelect the correct answer using the code given below:",
        "option_a": "1 and 2 only",
        "option_b": "2 and 3 only",
        "option_c": "1 and 3 only",
        "option_d": "1, 2 and 3",
        "correct_option": "A",
        "explanation": "A Constitutional Amendment Bill under Art 368 does NOT require the prior recommendation of the President; it can be introduced in either House by a minister or a private member. Bills under Art 3 and Art 117(1) require prior recommendation."
    }
]

def seed():
    with app.app_context():
        # Create all tables if not exist
        db.create_all()

        existing_count = QuizQuestion.query.count()
        print(f"Current questions in DB: {existing_count}")

        added = 0
        for item in questions_data:
            exists = QuizQuestion.query.filter_by(question=item["question"]).first()
            if not exists:
                q = QuizQuestion(
                    question=item["question"],
                    option_a=item["option_a"],
                    option_b=item["option_b"],
                    option_c=item["option_c"],
                    option_d=item["option_d"],
                    correct_option=item["correct_option"],
                    explanation=item["explanation"],
                    topic=item["topic"]
                )
                db.session.add(q)
                added += 1

        db.session.commit()
        total_now = QuizQuestion.query.count()
        print(f"Added {added} new questions. Total in database: {total_now}")

if __name__ == "__main__":
    seed()
