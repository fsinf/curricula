# Machine-readable TU Informatics Curricula

We maintain this data as XML because it can be easily validated against an XML
Schema Definition (XSD) (e.g. `xmllint --schema curriculum.xsd e033534.xml`).

The XML files in this repository are available at:

* https://www.fsinf.at/files/curricula/index.xml
* https://www.fsinf.at/files/curricula/e033534.xml

For more convenient consumption the files are also provided as JSON (they are
converted with `tojson.py`):

* https://www.fsinf.at/files/curricula/index.json
* https://www.fsinf.at/files/curricula/e033534.json

## Background

As the [informatics students council](https://www.fsinf.at/) we want to provide
a good tool to plan your studies to our students because TISS fails to do so.
Because our faculty does not have the necessary data in a machine-readable
format, we maintain it ourselves in this repository, so that we can provide our
students with the tool they deserve.

The legally binding TU Vienna curricula are only published as PDFs in TISS.
The semantics of these PDFs can only be extracted by relying on their
formatting which is not only inconsistent but also may change.
It is also important to note that the curricula PDFs can be out of date
because smaller changes are only announced in the [newsletter](https://tiss.tuwien.ac.at/mbl/main/)
and updated in TISS but don't make it into the PDFs.

While TISS has the curricula data in a machine-readable format, it does not
provide an API for it.  For larger changes to a curriculum a special provision,
[*Übergangsbestimmung*](http://www.informatik.tuwien.ac.at/studium/angebot/studienplaene),
is published that applies to all students admitted before the changes came into
effect.  Although Übergangsbestimmungen are very important for students, TISS
knows nothing about them.
