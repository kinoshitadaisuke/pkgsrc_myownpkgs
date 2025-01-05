# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-japanese-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for Japanese input methods
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# converters
DEPENDS+=	nkf>=0:../../converters/nkf
DEPENDS+=	skf>=0:../../converters/skf

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29

# fonts
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

# input methods
DEPENDS+=	mozc-elisp>=0:../../inputmethod/mozc-elisp
DEPENDS+=	mozc-server>=0:../../inputmethod/mozc-server
DEPENDS+=	mozc-tool>=0:../../inputmethod/mozc-tool

# textproc
DEPENDS+=	aspell>=0:../../textproc/aspell
DEPENDS+=	aspell-en>=0:../../textproc/aspell-en
DEPENDS+=	chasen>=0:../../textproc/chasen
DEPENDS+=	mecab>=0:../../textproc/mecab
DEPENDS+=	namazu>=0:../../textproc/namazu

# pkgsrc_myownpkgs
DEPENDS+=	bizter-ttf>=0:../../pkgsrc_myownpkgs/bizter-ttf
DEPENDS+=	cica-ttf>=0:../../pkgsrc_myownpkgs/cica-ttf
DEPENDS+=	firge-ttf>=0:../../pkgsrc_myownpkgs/firge-ttf
DEPENDS+=	hackgen-ttf>=0:../../pkgsrc_myownpkgs/hackgen-ttf
DEPENDS+=	juisee-ttf>=0:../../pkgsrc_myownpkgs/juisee-ttf
DEPENDS+=	plemoljp-ttf>=0:../../pkgsrc_myownpkgs/plemoljp-ttf
DEPENDS+=	udev-gothic-ttf>=0:../../pkgsrc_myownpkgs/udev-gothic-ttf
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
