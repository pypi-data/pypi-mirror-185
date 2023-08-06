from . import abc_dcml, bps, haydnsun, keymodt, mps, tavern, wir, wirwtc

available_collections = {
    "abc": abc_dcml,
    "bps": bps,
    "haydnsun": haydnsun,
    "keymodt": keymodt,
    "mps": mps,
    "tavern": tavern,
    "wir": wir,
    "wirwtc": wirwtc,
}


def getAnnotationScoreDataset(collections=[]):
    """

    Parameters
    ----------
    collections :
        Default value = [])

    Returns
    -------

    """
    allCollections = list(available_collections.keys())
    collections = collections or allCollections
    duples = {}
    splits = {"training": [], "validation": [], "test": []}
    for collection in collections:
        if collection not in allCollections:
            raise KeyError()
        module = available_collections[collection]
        duples.update(module.annotation_score_duples)
        for split in splits:
            splits[split].extend(module.splits[split])
    return duples, splits
