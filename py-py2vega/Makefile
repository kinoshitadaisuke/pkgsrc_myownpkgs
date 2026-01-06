# $NetBSD$

DISTNAME=	py2vega-0.6.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/py2vega/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/QuantStack/py2vega
COMMENT=	Python to Vega-expression transpiler
LICENSE=	modified-bsd

DEPENDS+=	${PYPKGPREFIX}-gast>=0.4.0:../../devel/py-gast

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
