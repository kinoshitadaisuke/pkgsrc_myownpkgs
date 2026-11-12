# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-audio-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs audio
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for audio
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# audio
DEPENDS+=	abcmidi>=0:../../audio/abcmidi
DEPENDS+=	audacious>=0:../../audio/audacious
DEPENDS+=	cmus>=0:../../audio/cmus
DEPENDS+=	easytag>=0:../../audio/easytag
DEPENDS+=	faad2>=0:../../audio/faad2
DEPENDS+=	fluidsynth>=0:../../audio/fluidsynth
DEPENDS+=	id3v2>=0:../../audio/id3v2
DEPENDS+=	lame>=0:../../audio/lame
DEPENDS+=	moc>=0:../../audio/moc
DEPENDS+=	mpg123>=0:../../audio/mpg123
DEPENDS+=	mpg321>=0:../../audio/mpg321
DEPENDS+=	musescore>=0:../../audio/musescore
#DEPENDS+=	quodlibet>=0:../../audio/quodlibet
DEPENDS+=	rhythmbox>=0:../../audio/rhythmbox
DEPENDS+=	rosegarden>=0:../../audio/rosegarden
DEPENDS+=	sox_ng>=0:../../audio/sox_ng
DEPENDS+=	timidity>=0:../../audio/timidity
DEPENDS+=	vorbis-tools>=0:../../audio/vorbis-tools
DEPENDS+=	xmms>=0:../../audio/xmms
DEPENDS+=	${PYPKGPREFIX}-music21>=0:../../audio/py-music21

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
