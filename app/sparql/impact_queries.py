IMPACT_BY_JURISDICTION = """
PREFIX trm: <urn:vertex:trm:>
PREFIX grip: <urn:vertex:grip:>

SELECT ?update ?rule WHERE {{
  ?update a grip:RegulatoryUpdate ;
          grip:impactsRule ?rule .
  ?rule trm:appliesToJurisdiction "{jurisdiction}" .
}}
"""