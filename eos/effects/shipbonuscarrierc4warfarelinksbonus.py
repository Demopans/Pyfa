# shipBonusCarrierC4WarfareLinksBonus
#
# Used by:
# Ship: Chimera
type = "passive"


def handler(fit, src, context):
    attrs = ["warfareBuff1Value", "warfareBuff2Value", "warfareBuff3Value", "warfareBuff4Value", "buffDuration"]
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Command") or mod.item.requiresSkill("Information Command"),
                                  attrs, src.getModifiedItemAttr("shipBonusCarrierC4"), skill="Caldari Carrier")
