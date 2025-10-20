# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-video-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs multimedia
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for video players and editors
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# multimedia
DEPENDS+=	ffmpeg2>=0:../../multimedia/ffmpeg2
DEPENDS+=	ffmpeg3>=0:../../multimedia/ffmpeg3
DEPENDS+=	ffmpeg4>=0:../../multimedia/ffmpeg4
DEPENDS+=	ffmpeg5>=0:../../multimedia/ffmpeg5
DEPENDS+=	ffmpeg6>=0:../../multimedia/ffmpeg6
DEPENDS+=	ffmpeg7>=0:../../multimedia/ffmpeg7
DEPENDS+=	ffmpeg8>=0:../../multimedia/ffmpeg8
DEPENDS+=	mplayer>=0:../../multimedia/mplayer
DEPENDS+=	mpv>=0:../../multimedia/mpv
#DEPENDS+=	olive-editor>=0:../../multimedia/olive-editor

.include "../../mk/bsd.pkg.mk"
