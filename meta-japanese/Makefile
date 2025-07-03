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
#DEPENDS+=	emacs29>=0:../../editors/emacs29
DEPENDS+=	emacs30>=0:../../editors/emacs30

# input methods
DEPENDS+=	mozc-elisp226>=0:../../inputmethod/mozc-elisp
DEPENDS+=	mozc-server226>=0:../../inputmethod/mozc-server
DEPENDS+=	mozc-tool226>=0:../../inputmethod/mozc-tool
DEPENDS+=	uim>=0:../../inputmethod/uim
DEPENDS+=	uim-mozc>=0:../../inputmethod/uim-mozc

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
