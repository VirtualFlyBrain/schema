from collections import namedtuple


opm = namedtuple("opm", ["cypher","entity"])


class QueryGenerator(object):

    def __init__(self):
        self.minimal_entity_info = "{short_form: %s.short_form, label: %s.label, " \
                           "iri: %s.iri, labels: labels(%s)}"

        self.synonym_match = "OPTIONAL MATCH(a)-[rp:has_reference]->(p:pub) " \
                        "WHERE rp.typ = 'def, WITH %s, " % w

        self.pub = "{ core: %s, microref: p.microref, PubMed: p.PMID, " \
              "FlyBase: p.FlyBase, DOI: p.DOI, ISBN: p.ISBN }"

        self.synonym = "{ label: rp.synonym, scope: rp.scope, type: rp.cat }"

        self.xrefs = "OPTIONAL MATCH(s:Site) < -[dbx:hasDbXref]-(a) WITH %s, " \
                "COLLECT({link: s.link_base + dbx.accession, link_text: s.label, " \
                "site: %s }) as xrefs" % (w, minimal_entity_info)

        self.images = "OPTIONAL MATCH(a)<-[:SUBCLASSOF|INSTANCEOF*]-(i:Individual)<-[:depicts]-" \
                 "(:Individual)-[irw:in_register_with]->(template:Individual)-[:depicts]->" \
                 "(template_anat:Individual) WITH limit %s 5, " \
                 "COLLECT({short_form: i.short_form, label: i.label," \
                 "template: template.label, folder: irw.folder, index: irw.index}" \
                 ") as images" % w

        self.term = "{core: %s }, description: a.description[0], comment: a.comment[0]} as term, %s" % (
        minimal_entity_info, w)
        return

    def roll_query(self, clauses):
        # for each clause
        return



minimal_entity_info = "{ short_form: o.short_form, label: o.label, iri: o.iri, labels: labels(o)}"

w = ''

primary_match = "MATCH(a:Class {short_form: %s }) WITH a "

rels= opm(var="rels",
          cypher="OPTIONAL MATCH(o:Class)<-[r]-(a:Class) WITH %s, " \
     "COLLECT ({ relation: r.label, object: %s } rels"  % (w, minimal_entity_info))

# Really need an edge property that distinguishes logical from annotation properties!
# TODO - Add retain related property to edge flipping code.Nico to add to V2.




