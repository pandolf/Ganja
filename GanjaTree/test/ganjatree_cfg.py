import FWCore.ParameterSet.Config as cms

process = cms.Process("Ganja")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 20


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.TFileService = cms.Service("TFileService",
      fileName = cms.string("ganjaTree.root"),
      closeFileFast = cms.untracked.bool(True)
)


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/work/p/pandolf/public/QCD_Pt50to80_CMSSW_5_3_32.root'
    )
)

process.ganja = cms.EDAnalyzer('GanjaTree'
)


process.p = cms.Path(process.ganja)
