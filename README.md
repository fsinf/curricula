# Machine-readable TU Informatics Curricula

The [Fachschaft Informatik](https://www.fsinf.at/) maintains machine-readable
versions of the TU Informatics Curricula because the faculty of informatics
fails to do so. The data is maintained in XML [on GitHub](https://github.com/fsinf/curricula)
and converted to JSON for easier consumption.

**THE DATA IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**

For the authoritative sources please consult the official curricula PDFs,
the [*Übergangsbestimmungen*][ubs] and the [TISS newsletter][newsletter].
If something seems off with an XML or JSON version, please [open an GitHub issue](https://github.com/fsinf/curricula/issues).

<!--table-->

The index of all curriculas is available as
[HTML](https://www.fsinf.at/files/curricula/),
[XML](https://www.fsinf.at/files/curricula/index.xml) and
[JSON](https://www.fsinf.at/files/curricula/index.json).

Additionally a [JavaScript API](https://www.fsinf.at/files/curricula/api.js) is provided.
You can try it out on the [web index](https://www.fsinf.at/files/curricula/)
by opening the developer console with F12 and running `await Curricula.getCurriculum('e033534')`.

## Terminology

* `required`, this group is required to complete the parent group
* `requires`, to do a course of this group you firstly need to complete the given group
* `minEcts`, to complete this group you need to complete at least the given
  amount of ECTS of courses within it (including subgroups)
* `maxEcts`, of the courses in this module you may only use the given amount of
  ECTS as part of this group
* `maxEctsIfUncompleted` as long as this group is uncompleted you may only do the
  given amount of ECTS from it (this only limits non-required subgroups)
* `variable`, courses can be used for this group that are not listed here

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
because smaller changes are only announced in the [newsletter][newsletter]
and updated in TISS but don't make it into the PDFs.

While TISS has the curricula data in a machine-readable format, it does not
provide an API for it.  For larger changes to a curriculum a special provision,
[*Übergangsbestimmung*][ubs],
is published that applies to all students admitted before the changes came into
effect.  Although Übergangsbestimmungen are very important for students, TISS
knows nothing about them.

[ubs]: http://www.informatik.tuwien.ac.at/studium/angebot/studienplaene
[newsletter]: https://tiss.tuwien.ac.at/mbl/main/

## Contributing

Issues and pull requests are welcome!

Please validate curricula against the schema, e.g.

	xmllint --schema curriculum.xsd e033534.xml
