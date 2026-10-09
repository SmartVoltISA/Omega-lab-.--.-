# Geometry Foundation Full Run 2026-10-10
Status: executed; independent operationalization where source code was absent.

Base seed: 20261010
Python: 3.12.15
NumPy: 2.5.3

## EXP-001

{
  "accuracy": {
    "boundary": {
      "mean": 0.21430333333333337,
      "n": 30,
      "sd": 0.061949002849303304
    },
    "flat": {
      "mean": 0.14599333333333334,
      "n": 30,
      "sd": 0.04159890112385955
    },
    "grow": {
      "mean": 0.21473333333333333,
      "n": 30,
      "sd": 0.06154031806162881
    },
    "memory": {
      "mean": 0.21473333333333333,
      "n": 30,
      "sd": 0.06154031806162881
    }
  },
  "note": "Independent ledger-scale rerun, not source-identical.",
  "states": {
    "mean": 20.7,
    "n": 30,
    "sd": 3.8160279041848266
  }
}

## EXP-002

{
  "note": "Toy ring; recurrence is not historical-state return.",
  "trace_delta": {
    "mean": 1.125,
    "n": 30,
    "sd": 0.0
  }
}

## EXP-003

{
  "conductance": {
    "mean": 0.080024,
    "n": 50,
    "sd": 0.003928262845023464
  },
  "f1": {
    "mean": 1.0,
    "n": 50,
    "sd": 0.0
  },
  "note": "Hidden modules are present in generator; not spontaneous emergence."
}

## EXP-004

{
  "0.1": {
    "conductance": {
      "mean": 0.09925824061340999,
      "n": 30,
      "sd": 0.003269497741851521
    },
    "f1": {
      "mean": 1.0,
      "n": 30,
      "sd": 0.0
    },
    "heldout_within": {
      "mean": 0.9006222222222223,
      "n": 30,
      "sd": 0.006080389514981351
    }
  },
  "0.2": {
    "conductance": {
      "mean": 0.1999333249989582,
      "n": 30,
      "sd": 0.004418498342569421
    },
    "f1": {
      "mean": 1.0,
      "n": 30,
      "sd": 0.0
    },
    "heldout_within": {
      "mean": 0.8000333333333334,
      "n": 30,
      "sd": 0.008850114184167176
    }
  },
  "0.3": {
    "conductance": {
      "mean": 0.3004708921948576,
      "n": 30,
      "sd": 0.0050783427222206206
    },
    "f1": {
      "mean": 1.0,
      "n": 30,
      "sd": 0.0
    },
    "heldout_within": {
      "mean": 0.7008666666666665,
      "n": 30,
      "sd": 0.009190866697506881
    }
  },
  "0.4": {
    "conductance": {
      "mean": 0.398441471850648,
      "n": 30,
      "sd": 0.005110185843604481
    },
    "f1": {
      "mean": 1.0,
      "n": 30,
      "sd": 0.0
    },
    "heldout_within": {
      "mean": 0.5980777777777778,
      "n": 30,
      "sd": 0.011724710563733361
    }
  },
  "0.45": {
    "conductance": {
      "mean": 0.44973955077718053,
      "n": 30,
      "sd": 0.008974485971852178
    },
    "f1": {
      "mean": 0.9944444444444446,
      "n": 30,
      "sd": 0.030429030972509218
    },
    "heldout_within": {
      "mean": 0.5498888888888889,
      "n": 30,
      "sd": 0.011422345959942203
    }
  },
  "note": "Planted-module positive control."
}

## EXP-005

{
  "candidate_cut": {
    "mean": 0.547622381119056,
    "n": 30,
    "sd": 0.010192641062889795
  },
  "note": "Fresh homogeneous generator; partition is not automatically meaningful.",
  "shuffled_cut": {
    "mean": 0.5210293848025734,
    "n": 30,
    "sd": 0.008677056560379353
  }
}

## EXP-006

{
  "homogeneous": {
    "learned_crossing_after": {
      "mean": 0.5,
      "n": 40,
      "sd": 0.0
    },
    "learned_crossing_baseline": {
      "mean": 0.4445704345164101,
      "n": 40,
      "sd": 0.09777638849480556
    },
    "learned_crossing_delta": {
      "mean": 0.055429565483589925,
      "n": 40,
      "sd": 0.09777638849480556
    },
    "random_crossing_after": {
      "mean": 0.5,
      "n": 40,
      "sd": 0.0
    },
    "random_crossing_baseline": {
      "mean": 0.5066502297687119,
      "n": 40,
      "sd": 0.10628318131911675
    },
    "random_crossing_delta": {
      "mean": -0.006650229768711838,
      "n": 40,
      "sd": 0.10628318131911675
    }
  },
  "modular": {
    "learned_crossing_after": {
      "mean": 0.5,
      "n": 40,
      "sd": 0.0
    },
    "learned_crossing_baseline": {
      "mean": 0.15,
      "n": 40,
      "sd": 0.0
    },
    "learned_crossing_delta": {
      "mean": 0.35,
      "n": 40,
      "sd": 0.0
    },
    "learned_f1": {
      "mean": 1.0,
      "n": 40,
      "sd": 0.0
    },
    "random_crossing_after": {
      "mean": 0.5,
      "n": 40,
      "sd": 0.0
    },
    "random_crossing_baseline": {
      "mean": 0.49854166666666655,
      "n": 40,
      "sd": 0.0692575476463244
    },
    "random_crossing_delta": {
      "mean": 0.0014583333333333989,
      "n": 40,
      "sd": 0.0692575476463244
    }
  },
  "note": "Exploratory intervention proxy; not causal-boundary certification."
}

Limits: EXP-003/004 use planted modules; EXP-005 partition is not automatically meaningful; EXP-006 is exploratory; none of these toy tests establishes a universal physical law.
Raw per-seed results are in GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.json.
