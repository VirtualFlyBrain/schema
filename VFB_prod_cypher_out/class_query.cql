MATCH (a:Class { short_form: 'FBbt_00003632'}) WITH a
      OPTIONAL MATCH (o:Class)<-[r]-(a)  with a, // Really need an edge property that distinguishes logical from annotation properties!
      COLLECT ({ relation: r.label, object:
	    { short_form: o.short_form, label:  o.label, iri: o.iri, labels: labels(o) } }) as rels   
     OPTIONAL MATCH (a)-[rp:has_reference]->(p:pub) WITH a, rels,
      COLLECT ({ relation: rp.typ, pub:
		{ core: { short_form: p.short_form, label:  p.label, iri: p.iri, labels: labels(p) },
		 microref: p.microref, PubMed: p.PMID, FlyBase: p.FlyBase, DOI: p.DOI, ISBN: p.ISBN },
	         synonym: { label: rp.synonym, scope: rp.scope, type: rp.cat}}
	       ) as pub_syn    
     OPTIONAL MATCH (s:Site)<-[dbx:hasDbXref]-(a)  WITH a, rels, pub_syn,
     COLLECT ({ link: s.link_base + dbx.accession, link_text: s.label,
	    site: { short_form: s.short_form, label:  s.label, iri: s.iri, labels: labels(s) }}) as xrefs 
     OPTIONAL MATCH (a)<-[:SUBCLASSOF|INSTANCEOF*]-(i:Individual)<-[:depicts]-(:Individual)-[irw:in_register_with]->(template:Individual)
WITH a, rels, pub_syn, xrefs, i, irw, template limit 5    
RETURN
       COLLECT ({ short_form: i.short_form, label: i.label, 
	   template: template.label, folder: irw.folder, index: irw.index }) as images,
      { core: { short_form: a.short_form, label:  a.label, iri: a.iri, labels: labels(a) }, description: a.description[0], comment: a.comment[0] } as term,
      xrefs, pub_syn, rels
     
