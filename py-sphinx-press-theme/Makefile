# $NetBSD$

DISTNAME=	sphinx_press_theme-0.8.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/sphinx_press_theme/sphinx-press-theme/}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sphinx_press_theme/}

MAINTAINER=	INSERT_YOUR_MAIL_ADDRESS_HERE # or use pkgsrc-users@NetBSD.org
HOMEPAGE=	https://schettino72.github.io/sphinx_press_site/
COMMENT=	A Sphinx-doc theme based on Vuepress
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-sphinx>=4.0.1:../../textproc/py-sphinx

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
