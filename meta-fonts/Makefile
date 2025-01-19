# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-fonts-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs fonts
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	cyberbit-ttf>=0:../../fonts/cyberbit-ttf
DEPENDS+=	intlfonts>=0:../../fonts/intlfonts
DEPENDS+=	freefont-ttf>=0:../../fonts/freefont-ttf
DEPENDS+=	motoya-fonts>=0:../../fonts/motoya-fonts
DEPENDS+=	mozilla-fonts>=0:../../fonts/mozilla-fonts
#DEPENDS+=	noto-cjk-fonts>=0:../../fonts/noto-cjk-fonts
#DEPENDS+=	noto-fonts>=0:../../fonts/noto-fonts
DEPENDS+=	noto-ttf>=0:../../fonts/noto-ttf

# Japanese fonts
DEPENDS+=	ipaexfont>=0:../../fonts/ipaexfont
DEPENDS+=	ipafont>=0:../../fonts/ipafont
DEPENDS+=	ja-dotgothic16-ttf>=0:../../fonts/ja-dotgothic16-ttf
DEPENDS+=	ja-elisat>=0:../../fonts/ja-elisat
DEPENDS+=	ja-elisau>=0:../../fonts/ja-elisau
DEPENDS+=	ja-kaname>=0:../../fonts/ja-kaname
DEPENDS+=	ja-kappa20>=0:../../fonts/ja-kappa20
DEPENDS+=	ja-klee-ttf>=0:../../fonts/ja-klee-ttf
DEPENDS+=	ja-naga10>=0:../../fonts/ja-naga10
DEPENDS+=	ja-rampart-ttf>=0:../../fonts/ja-rampart-ttf
DEPENDS+=	ja-reggae-ttf>=0:../../fonts/ja-reggae-ttf
DEPENDS+=	ja-rocknroll-ttf>=0:../../fonts/ja-rocknroll-ttf
DEPENDS+=	ja-sazanami-ttf>=0:../../fonts/ja-sazanami-ttf
DEPENDS+=	ja-shinonome>=0:../../fonts/ja-shinonome
DEPENDS+=	ja-stick-ttf>=0:../../fonts/ja-stick-ttf
DEPENDS+=	ja-train-ttf>=0:../../fonts/ja-train-ttf
DEPENDS+=	jisx0208fonts>=0:../../fonts/jisx0208fonts
DEPENDS+=	jisx0212fonts>=0:../../fonts/jisx0212fonts
DEPENDS+=	jisx0213fonts>=0:../../fonts/jisx0213fonts
DEPENDS+=	kiloji-ttf>=0:../../fonts/kiloji-ttf
DEPENDS+=	kochi-ttf>=0:../../fonts/kochi-ttf
DEPENDS+=	konatu-ttf>=0:../../fonts/konatu-ttf
DEPENDS+=	koruri-ttf>=0:../../fonts/koruri-ttf
DEPENDS+=	ohruri-ttf>=0:../../fonts/ohruri-ttf
DEPENDS+=	ricty-ttf>=0:../../fonts/ricty-ttf
DEPENDS+=	takao-ex-fonts-ttf>=0:../../fonts/takao-ex-fonts-ttf
DEPENDS+=	takao-fonts-ttf>=0:../../fonts/takao-fonts-ttf
DEPENDS+=	umefont-ttf>=0:../../fonts/umefont-ttf
DEPENDS+=	vlgothic-ttf>=0:../../fonts/vlgothic-ttf
DEPENDS+=	watanabe-vfont>=0:../../fonts/watanabe_vfont

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
